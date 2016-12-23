figure(2)
for i=1:500 
  
    if  graph(i,4)==2
        scatter3(graph(i,1),graph(i,2),graph(i,3),'g');
        hold on
    end
    if  graph(i,4)==3
        scatter3(graph(i,1),graph(i,2),graph(i,3),'b');
        hold on
    end
   

    if  graph(i,4)==6
        scatter3(graph(i,1),graph(i,2),graph(i,3),'k');
        hold on
    end
    if  graph(i,4)==7
        scatter3(graph(i,1),graph(i,2),graph(i,3),'r+');
        hold on
    end
    if  graph(i,4)==8
        scatter3(graph(i,1),graph(i,2),graph(i,3),'g+');
        hold on
    end
    if  graph(i,4)==9
        scatter3(graph(i,1),graph(i,2),graph(i,3),'b+');
        hold on
    end
    if  graph(i,4)==10
        scatter3(graph(i,1),graph(i,2),graph(i,3),'c+');
        hold on
    end
    if  graph(i,4)==11
        scatter3(graph(i,1),graph(i,2),graph(i,3),'m+');
        hold on
    end
    if  graph(i,4)==12
        scatter3(graph(i,1),graph(i,2),graph(i,3),'y+');
        hold on
    end
    if  graph(i,4)==13
        scatter3(graph(i,1),graph(i,2),graph(i,3),'k+');
        hold on
    end
    if  graph(i,4)==14
        scatter3(graph(i,1),graph(i,2),graph(i,3),'r>');
        hold on
    end
    if  graph(i,4)==0
        scatter3(graph(i,1),graph(i,2),graph(i,3),'g>');
        hold on
    end
end
hold off
title('500 stocks cluster')