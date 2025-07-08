hanoi(0, _, _, _) :- !.
hanoi(N, From, To, Aux) :-
    N > 0,
    M is N - 1,
    hanoi(M, From, Aux, To),
    format('Move disk ~w from ~w to ~w~n', [N, From, To]),
    hanoi(M, Aux, To, From).





?- hanoi(2, left, right, center).
