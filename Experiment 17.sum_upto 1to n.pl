sum_upto(0,0).
sum_upto(N,Sum):-
N>0,
N1 is N-1,
sum_upto(N1,Sum1),
Sum is Sum1+N.
