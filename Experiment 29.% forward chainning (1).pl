% Known facts
fact(sun_is_shining).
fact(weather_is_hot).

% Rules: rule(NewFact, [Condition1, Condition2, ...])
rule(go_for_swimming, [sun_is_shining, weather_is_hot]).
rule(drink_water, [weather_is_hot]).
rule(wear_cap, [sun_is_shining]).

% Forward chaining main rule
forward :-
    rule(Fact, Conditions),
    \+ fact(Fact),         % If Fact not already known
    check_all(Conditions), % Check if all conditions are true
    assert(fact(Fact)),    % Add new fact
    write('New fact: '), write(Fact), nl,
    forward.               % Repeat
forward.                   % Stop when no more new facts
