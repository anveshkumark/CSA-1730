% Initial state: monkey on floor at door, box in middle, monkey has nothing
% Goal: monkey has banana

% Define steps to reach banana
can_get_banana :-
    write('Monkey walks to middle'), nl,
    write('Monkey pushes box to banana'), nl,
    write('Monkey climbs box'), nl,
    write('Monkey takes banana'), nl.
