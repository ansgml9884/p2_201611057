%%plantuml
@startuml
start
:set how many turns;
:set how much to grow bigger;
:set angle;
:set start size;
repeat
if (i is divided by 2) then
    :grow bigger;
endif
:draw;
repeat while(turns)
stop
@enduml