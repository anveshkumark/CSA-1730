% Known facts
fact(sun_is_shining).
fact(weather_is_hot).

% Rules
rule(go_for_swimming, [sun_is_shining, weather_is_hot]).
rule(drink_water, [weather_is_hot]).
rule(wear_cap, [sun_is_shining]).

% Backward chaining
backward(Goal) :-
    fact(Goal),                        % Check if Goal is a known fact
    write('Known: '), write(Goal), nl.

backward(Goal) :-
    rule(Goal, Conditions),            % Find rule for the Goal
    check_all(Conditions),            % Prove all conditions
    write('Inferred: '), write(Goal), nl.

% Check each condition
check_all([]).
check_all([H|T]) :-
    backward(H),
    check_all(T).
