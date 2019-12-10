vedio_r = VideoWriter([lrs_conf.lrs_dir, '/defect_r.avi']);
vedio_g = VideoWriter([lrs_conf.lrs_dir, '/defect_g.avi']);
vedio_b = VideoWriter([lrs_conf.lrs_dir, '/defect_b.avi']);

vedio_r.FrameRate = 5;
vedio_g.FrameRate = 5;
vedio_b.FrameRate = 5;

open(vedio_r);
open(vedio_g);
open(vedio_b);

diro=dir(fullfile('/media/dong/data1/Ning_Shaochun/FgSegNet_v2科研/KDE+SVM+大量/data/','*.jpg'));

for i=1:length(diro)  %图像序列个数
    fname=strcat('/media/dong/data1/Ning_Shaochun/FgSegNet_v2科研/KDE+SVM+大量/data/',diro(i).name);
    frame = imread(fname);
    r=frame(:,:,1);
    g=frame(:,:,2);
    b=frame(:,:,3);
    writeVideo(vedio_r,r);
    writeVideo(vedio_g,g);
    writeVideo(vedio_b,b);
    
    disp(fname);
    
end

close(vedio_r);
close(vedio_g);
close(vedio_b);
