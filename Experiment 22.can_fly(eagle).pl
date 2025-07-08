can_fly(eagle).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).

fly(bird) :- can_fly(Bird), write('Yes, can fly').
fly(bird) :- cannot_fly(Bird), write('No, cannot fly').
fly(bird) :- write('Unknown if can fly').
