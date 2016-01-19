% main control code - assumes full state knowledge
%
%
% Modified: 
%   2/11/2014 - R. Beard
%   2/18/2014 - R. Beard
%   2/24/2014 - R. Beard
%   1/4/2016  - R. Beard
%

% this first function catches simulink errors and displays the line number
function v_c=controller_home(uu,P)
    try
        v_c=controller_home_(uu,P);
    catch e
        msgString = getReport(e);
        fprintf(2,'\n%s\n',msgString);
        rethrow(e);
    end
end

% main control function
function v_c=controller_home_(uu,P)

    % process inputs to function
    % robots - own team
    for i=1:P.num_robots,
        robot(:,i)   = uu(1+3*(i-1):3+3*(i-1));
    end
    NN = 3*P.num_robots;
    % robots - opponent
    for i=1:P.num_robots,
        opponent(:,i)   = uu(1+3*(i-1)+NN:3+3*(i-1)+NN);
    end
    NN = NN + 3*P.num_robots;
    % ball
    ball = [uu(1+NN); uu(2+NN)];
    NN = NN + 2;
    % score: own team is score(1), opponent is score(2)
    score = [uu(1+NN); uu(2+NN)];
    NN = NN + 2;
    % current time
    t      = uu(1+NN);

    % robot #1 positions itself behind ball and rushes the goal.
    %v1 = play_rush_goal(robot(:,1), ball, P);
    v1 = skill_block_opponent_goalie(robot(:, 1), opponent(:, 2), P);
    % robot #2 stays at the goal, defending it
    v2 = skill_defend_goal(robot(:, 2), ball, opponent(:, 1), P);
    
    % output velocity commands to robots
    v1 = utility_saturate_velocity(v1,P);
    v2 = utility_saturate_velocity(v2,P);
    v_c = [v1; v2];
end

%-----------------------------------------
% play - rush goal
%   - go to position behind ball
%   - if ball is between robot and goal, go to goal
% NOTE:  This is a play because it is built on skills, and not control
% commands.  Skills are built on control commands.  A strategy would employ
% plays at a lower level.  For example, switching between offense and
% defense would be a strategy.
function v = play_rush_goal(robot, ball, P)
  
  % normal vector from ball to goal
  n = P.goal-ball;
  n = n/norm(n);
    
  % compute position 10cm behind ball, but aligned with goal.
  position = ball - 0.2*n;
  
  if norm(position-robot(1:2))<.21,
      v = skill_go_to_point(robot, P.goal, P);
  else
      v = skill_go_to_point(robot, position,P);
  end

end

%-----------------------------------------
% skill - follow ball on line
%   follows the y-position of the ball, while maintaining x-position at
%   x_pos.  Angle always faces the goal.

function v=skill_follow_ball_on_line(robot, ball, x_pos, P)

    % control x position to stay on current line
    vx = -P.control_k_vx*(robot(1)-x_pos);
    
    % control y position to match the ball's y-position
    vy = -P.control_k_vy*(robot(2)-ball(2));

    % control angle to -pi/2
    theta_d = atan2(P.goal(2)-robot(2), P.goal(1)-robot(1));
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    v = [vx; vy; omega];
end

%/////////////////////////////////////////
%            NEW CODE
%/////////////////////////////////////////

%-----------------------------------------
% Helper function - Get Ball Direction
%   gets the direction that the ball is moving in by returning the
%   difference between its old and new position every third of a second.

function difference=getBallVec(ball)
    %figure out where the ball is heading
    persistent oldBallPos;
    persistent currBallPos;
    persistent count;
    if isempty(count)
      count = 0 ;
      oldBallPos = zeros(1,2);
      currBallPos = zeros(1,2);
    end
    if (count > 30)
    oldBallPos = currBallPos;
    currBallPos = ball;
    %disp(['old is: ' num2str(oldBallPos(1))]);
    %disp(['curr is: ' num2str(currBallPos(1))]);
    count = 0;
    end
    count = count + 1;
    difference = currBallPos(1) - oldBallPos(1);
end

%-----------------------------------------
% skill - Block oppoenent goalie
%   has the attacker robot rush to the opponent goalie and block him so
%   the goal would be wide open for the offensive goalie to take the shot.

function v=skill_block_opponent_goalie(robot, opponent, P)
    v = skill_go_to_point(robot, opponent, P);
end

%-----------------------------------------
% skill - offensive goalie
%   has the defender robot hit the ball if the ball is on the opponent's
%   field, else the robot stays on a designated defense line.
function v=skill_offensive_Goalie(robot, ball, opponent, P)
    direction = getBallVec(ball); % Get the direction of the ball   
    if (ball(1) < 0) % ball is on our side, defend goal
        v = skill_defend_goal(robot, ball, opponent, P);
    elseif (direction < 0) % if ball is heading towards us
        % have the attacked robot block the goalie and hit the ball
        v = play_rush_goal(robot, ball, P);
    else
        v = skill_follow_ball_on_line(robot, ball, -P.field_width/4, P);
    end
end

%-----------------------------------------
% skill - normal goalie
%   has the defense robot rush back to the goal to defend it by matching
%   the y-position of the ball (limited to the goal's edges) and matching
%   the angle to the direction the ball is coming from
function v=skill_normal_Goalie(robot, ball, P)
    % Create a point using the coordinates of the home goal
    point = zeros(1,2);
    point(1,1) = -P.field_width;
    point(1,2) = 0;
    
     % control angle to -pi/2
    theta_d = atan2(ball(2)-robot(2), ball(1)-robot(1));
    if (theta_d < -pi/2)
        theta_d = -pi/2;
    elseif (theta_d > pi/2)
        theta_d = pi/2;
    end
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
     % get back to the home goal
    v = skill_go_to_point(robot, point, P);
    
    % match the y position of the ball
    v(2) = -P.control_k_vy*(robot(2)-ball(2));
    
    % restrict movement to the goal edges
    if (ball(2) > P.goal_width/2)
        point(1,2) = P.goal_width/2;
        v = skill_go_to_point(robot, point, P);
    end
    if (ball(2) < -P.goal_width/2)
        point(1,2) = -P.goal_width/2;
        v = skill_go_to_point(robot, point, P);
    end
        
    % assign angle
    v(3) = omega;
end

%-----------------------------------------
% skill - defend goal
%   alternates between normal goalie and defensive goalie depending on the
%   position of the ball in the field.
function v=skill_defend_goal(robot, ball, opponent, P)

    direction = getBallVec(ball); % Get the direction of the ball
    % If ball is on the right half of the field and going towards them
    if (ball(1) > 0) 
        v=skill_offensive_Goalie(robot, ball, opponent, P);
    else
        v=skill_normal_Goalie(robot, ball, P);
    end
end

%/////////////////////////////////////////
%-----------------------------------------
% skill - go to point
%   follows the y-position of the ball, while maintaining x-position at
%   x_pos.  Angle always faces the goal.
function v=skill_go_to_point(robot, point, P)

    % control x position to stay on current line
    vx = -P.control_k_vx*(robot(1)-point(1));
    
    % control y position to match the ball's y-position
    vy = -P.control_k_vy*(robot(2)-point(2));

    % control angle to -pi/2
    theta_d = atan2(P.goal(2)-robot(2), P.goal(1)-robot(1));
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    v = [vx; vy; omega];
end


%------------------------------------------
% utility - saturate_velocity
% 	saturate the commanded velocity 
%
function v = utility_saturate_velocity(v,P)
    if v(1) >  P.robot_max_vx,    v(1) =  P.robot_max_vx;    end
    if v(1) < -P.robot_max_vx,    v(1) = -P.robot_max_vx;    end
    if v(2) >  P.robot_max_vy,    v(2) =  P.robot_max_vy;    end
    if v(2) < -P.robot_max_vy,    v(2) = -P.robot_max_vy;    end
    if v(3) >  P.robot_max_omega, v(3) =  P.robot_max_omega; end
    if v(3) < -P.robot_max_omega, v(3) = -P.robot_max_omega; end
end


  