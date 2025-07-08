% Graph connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Heuristic values (lower is better)
heuristic(a, 5).
heuristic(b, 3).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 3).
heuristic(f, 0).  % Goal node

% Best First Search
best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% If goal is reached
bfs([[Goal|T]|_], Goal, [Goal|T]).

% Expand first path and continue
bfs([[Current|T]|Rest], Goal, Path) :-
    findall([Next,Current|T],
        (edge(Current, Next), \+ member(Next, [Current|T])),
        NextPaths),
    append(Rest, NextPaths, NewQueue),
    sort_by_heuristic(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, Path).

% Sort paths using heuristic of the first node
sort_by_heuristic(Paths, Sorted) :-
    map_list_to_pairs(get_h, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

get_h([Node|_], H) :- heuristic(Node, H).
