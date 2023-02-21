cd /home/seewon/Webcat/detectors/a_academic && docker build -t seewon/webcat-a-academic . && docker push seewon/webcat-a-academic &
sleep 2
cd /home/seewon/Webcat/detectors/a_general && docker build -t seewon/webcat-a-general . && docker push seewon/webcat-a-general &
sleep 2
cd /home/seewon/Webcat/detectors/a_scholarship && docker build -t seewon/webcat-a-scholarship . && docker push seewon/webcat-a-scholarship &
sleep 2
cd /home/seewon/Webcat/detectors/g_cse_jobs && docker build -t seewon/webcat-g-cse-jobs . && docker push seewon/webcat-g-cse-jobs &
sleep 2
cd /home/seewon/Webcat/detectors/g_cse_main && docker build -t seewon/webcat-g-cse-main . && docker push seewon/webcat-g-cse-main &
sleep 2
cd /home/seewon/Webcat/detectors/g_ee_academic && docker build -t seewon/webcat-g-ee-academic . && docker push seewon/webcat-g-ee-academic &
sleep 2
cd /home/seewon/Webcat/detectors/g_ee_general && docker build -t seewon/webcat-g-ee-general . && docker push seewon/webcat-g-ee-general &
sleep 2
cd /home/seewon/Webcat/detectors/h_econ_general && docker build -t seewon/webcat-h-econ-general . && docker push seewon/webcat-h-econ-general &
sleep 2
cd /home/seewon/Webcat/detectors/i_biz_academic && docker build -t seewon/webcat-i-biz-academic . && docker push seewon/webcat-i-biz-academic &