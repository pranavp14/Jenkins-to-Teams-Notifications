* Settings *
Library             SeleniumLibrary
Library             ./teams-notification.py

* Variables *
${platform}            Dummy
${operation}           Dummy
${module}              Dummy
${cluster_name}        Dummy
${cluster_version}     Dummy
${cluster_param}       Dummy
${username}            Dummy
${job_name}            Dummy
${machine_ip}          Dummy
${build_name}          Dummy
${build_url}           Dummy
${project_url}         Dummy
${output_xml}          output.xml
${buildDurationMillis}     50000
${de/commissioning_job_name}    Cluster_Commission_Decommission
${test_channel}    https://testchannel.webhook.office.com/webhookb2/3bcb6302-ee74-410b-902f-5e22e@acce4151-9118-4e3b-8141-9a6210dbb561/IncomingWebhook/e428d882d78387639cad7da05f/807cff89-3da1-424b-9955-d11e56142   

        
* Test Cases *
Send Teams Notification for cluster commission decommission
    ${html_file}=    Generate Job Report To Cluster Commission Decommission    ${platform}    ${operation}    ${module}    ${cluster_name}    ${cluster_version}    ${cluster_param}    ${username}        
    Send Cluster Build Result Notification To Teams     ${test_channel}     ${html_file}    ${de/commissioning_job_name}    ${build_url}