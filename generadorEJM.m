function [xd,xdp,yd,ydp] = fcn(u)

r=0.3;
v=0.05;
w=v/r;


persistent t
if isempty(t)
    t=0;
end

    % tramo1
if and(t>=0,t<30)
    xd = 0;
    xdp = 0;
    yd = v*t;
    ydp = v;

    % tramo2
elseif and(t>=30,t<78) 
    xd = 0;
    xdp = 0;
    yd = v*t;
    ydp = v;

    % tramo3
elseif and(t>78,t<78+pi/(2*w))
    xd = r*cos(-w*t+pi)+0.3;
    xdp = r*sin(-w*t+pi)*w;
    yd = r*sin(-w*t+pi)+3.9;
    ydp = -r*cos(-w*t+pi)*w;
    
    % tramo4
elseif and(t>=78+pi/(2*w),t<78+pi/(2*w)+18)
    xd = v*(t-(78+pi/(2*w)))+0.3;
    xdp = v;
    yd = 4.2;
    ydp = 0;
    
    % tramo5
elseif and(t>=78+pi/(2*w)+18,t<96+pi/(2*w)+pi/(2*w))
    t5=(t-(78+2*pi/(2*w)));
    xd = r*cos(-w*t5+pi)+1.2;
    xdp = r*sin(-w*t5+pi)*w;
    yd = r*sin(-w*t5+pi)+3.9;
    ydp = -r*cos(-w*t5+pi)*w;
    
    % tramo6
elseif and(t>=114.8496,t<114.8496+12) 
    xd = 1.5;
    xdp = 0;
    yd = -v*(t-114.8496)+3.9;
    ydp = -v;
    
    % tramo7
elseif and(t>=114.8496+12,t<114.8496+12+pi/(2*w))
    t5=(t-(114.8496+12));
    xd = r*cos(-w*t5)+1.2;
    xdp = r*sin(-w*t5)*w;
    yd = r*sin(-w*t5)+3.3;
    ydp = -r*cos(-w*t5)*w;    

    % tramo8
elseif and(t>=114.8496+12+pi/(2*w),t<114.8496+12+pi/(2*w)+6)
    xd = -v*(t-(114.8496+12+pi/(2*w)))+1.2;
    xdp = -v;
    yd = 3;
    ydp = 0;
    
    % tramo9
elseif and(t>=114.8496+12+pi/(2*w)+6,t<114.8496+12+pi/(2*w)+6+pi/(2*w))
    t5=(t-(114.8496+12+pi/(2*w)+6));
    xd = r*cos(w*t5+pi/2)+1.05;
    xdp = -r*sin(w*t5+pi/2)*w;
    yd = r*sin(w*t5+pi/2)+2.7;
    ydp = r*cos(w*t5+pi/2)*w;    
    
    % tramo10
elseif and(t>=114.8496+12+pi/(2*w)+6+pi/(2*w),t<114.8496+12+pi/(2*w)+6+pi/(2*w)+24) 
    xd = 0.75;
    xdp = 0;
    yd = -v*(t-(114.8496+12+pi/(2*w)+6+pi/(2*w)))+2.7;
    ydp = -v;
    
% tramo11
elseif and(t>=114.8496+12+pi/(2*w)+6+pi/(2*w)+24,t<114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w))
    t5=(t-(114.8496+12+pi/(2*w)+6+pi/(2*w)+24));
    xd = r*cos(-w*t5)+0.45;
    xdp = r*sin(-w*t5)*w;
    yd = r*sin(-w*t5)+1.5;
    ydp = -r*cos(-w*t5)*w;    
    
    % tramo12
elseif and(t>=114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w),t<114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w)+3)
    xd = -v*(t-(114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w)))+0.45;
    xdp = -v;
    yd = 1.2;
    ydp = 0;
    
% tramo13
elseif and(t>=114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w)+3,t<114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w)+3+pi/(2*w))
    t5=(t-(114.8496+12+pi/(2*w)+6+pi/(2*w)+24+pi/(2*w)+3));
    xd = r*cos(-w*t5+3*pi/2)+0.3;
    xdp = r*sin(-w*t5+3*pi/2)*w;
    yd = r*sin(-w*t5+3*pi/2)+1.5;
    ydp = -r*cos(-w*t5+3*pi/2)*w;    


    % tramo14
elseif and(t>=197.5487,t<197.5487+48) 
    xd = 0;
    xdp = 0;
    yd = v*(t-197.5487)+1.5;
    ydp = v;
    
    
    
    % tramo4
elseif and(t>=197.5487+48,t<197.5487+48+9)
    xd = v*(t-(197.5487+48))+0;
    xdp = v;
    yd = 3.9;
    ydp = 0;
    
    % tramo4
elseif and(t>=197.5487+48+9,t<197.5487+48+9+15)
    xd = v*(t-(197.5487+48+9))+0.45;
    xdp = v;
    yd = 3.9;
    ydp = 0;
    
    % tramo5
elseif and(t>=197.5487+48+9+15,t<197.5487+48+9+15+pi/(2*w))
    t5=(t-(197.5487+48+9+15));
    xd = r*cos(-w*t5+pi)+1.05;
    xdp = r*sin(-w*t5+pi)*w;
    yd = r*sin(-w*t5+pi)+3.75;
    ydp = -r*cos(-w*t5+pi)*w;

    % tramo6
elseif and(t>=197.5487+48+9+15+pi/(2*w),t<197.5487+48+9+15+pi/(2*w)+6) 
    xd = 1.2;
    xdp = 0;
    yd = -v*(t-(197.5487+48+9+15+pi/(2*w)))+3.75;
    ydp = -v;
    
    % tramo7
elseif and(t>=197.5487+48+9+15+pi/(2*w)+6,t<197.5487+48+9+15+pi/(2*w)+6+pi/(2*w))
    t5=(t-(197.5487+48+9+15+pi/(2*w)+6));
    xd = r*cos(-w*t5)+1.05;
    xdp = r*sin(-w*t5)*w;
    yd = r*sin(-w*t5)+3.45;
    ydp = -r*cos(-w*t5)*w;    
    
    % tramo8
elseif and(t>=197.5487+48+9+15+pi/(2*w)+6+pi/(2*w),t<197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+15)
    xd = -v*(t-(197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)))+1.05;
    xdp = -v;
    yd = 3.3;
    ydp = 0;
    
% tramo13
elseif and(t>=197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+15,t<197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+pi/(2*w)+15)
    t5=(t-(197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+15));
    xd = r*cos(-w*t5+3*pi/2)+0.45;
    xdp = r*sin(-w*t5+3*pi/2)*w;
    yd = r*sin(-w*t5+3*pi/2)+3.45;
    ydp = -r*cos(-w*t5+3*pi/2)*w;    
    
    % tramo14
elseif and(t>=197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+pi/(2*w)+15,t<197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+pi/(2*w)+15+6) 
    xd = 0.3;
    xdp = 0;
    yd = v*(t-(197.5487+48+9+15+pi/(2*w)+6+pi/(2*w)+pi/(2*w)+15))+3.45;
    ydp = v;
    
else
    xd = 0.1;
    xdp = 0;
    yd = 0.25;
    ydp = 0;

end

t = t + 0.05;


% xd = r*cos(w*t-pi/2)-0.5;
% xdp = -r*sin(w*t-pi/2)*w;
% 
% yd = r*sin(w*t-pi/2)+0.5;
% ydp = r*cos(w*t-pi/2)*w;
