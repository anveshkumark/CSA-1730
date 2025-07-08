vowel(a).vowel(e).vowel(i).vowel(O).vowel(u).

count_vowels(S,C):-atom_chars(S,L),count(L,C).
count([],0).
count([H|T],C):-vowel(H),count(T,C1),C is C1+1.
count([_|T],C):-count(T,C).
