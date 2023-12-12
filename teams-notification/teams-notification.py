import xml.etree.ElementTree as ET
import requests
import json
from pathlib import Path
from SeleniumLibrary import *
from robot.api.deco import keyword
from robot.api import logger
import string
from robot.libraries.Collections import Collections
from robot.libraries.BuiltIn import BuiltIn

class teams_notification(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    @keyword
    def generate_job_report_to_cluster_commission_decommission(self, platform, operation, module, clusterName, clusterVersion, clusterParam, username):
        script_path = Path(_file_).resolve()
        parent_directory = script_path.parent
        cwd = str(parent_directory.parent)
        export_path_final = Path(cwd) / "output.xml"
        print(export_path_final)
        output_html_file = "cluster_commission_decommission_report.html"
        if export_path_final.exists():
            xml_file_path = export_path_final
            suite_data  =  self.parse_xml_report(xml_file_path)

            with open(output_html_file, 'w') as file:
                file.write('<html>\n<head>\n<title>"Cluster commission/decommission"</title>\n')
                file.write('</head>\n<body>\n')

                total_tests = 0
                total_passed = 0
                total_failed = 0

                for suite in suite_data:
                    total_tests += suite['total_count']
                    total_passed += suite['passed_count']
                    total_failed += suite['failed_count']

                if total_failed == 0:
                    file.write(f'<h3>Create TF-K8S-Cluster Status : <b style="color: #17594A;"> Successful</b></h3><br>\n')                
                else :
                    file.write(f'<h3>Create TF-K8S-Cluster Status : <b style="color: #FF0000"> Failed </b></h3><br>\n')

                file.write('<b>Cluster Details:</b> <br><br>'
                        f'Platform : {platform} <br>' +
                        f'Operation : {operation} <br>' +
                        f'Module : {module} <br>' +
                        f'Cluster_Name : {clusterName} <br>')
                
                if platform != 'k8s':
                        file.write(f'Cluster_Version : {clusterVersion} <br>')
                
                file.write(f'Cluster_Param : {clusterParam} <br>' +
                        f'Build User : {username} <br>')  
                 
                file.write('</body>\n</html>\n')

        else:
            print('No output.xml file was found in the directory.')
            with open(output_html_file, 'w') as file:
                file.write(f'<html>\n<head>\n<title>"Create TF-K8S-Cluster Status"</title>\n')
                file.write('</head>\n<body>\n')
                file.write(f'<p> output.xml file does not exist at the specified path.</p><br>')
                file.write('</body>\n</html>\n')
        
        return output_html_file
    

    def parse_xml_report(self,xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        suite_data = []
        for suite in root.iter('suite'):
            suite_name = suite.get('name')
            test_cases = suite.findall('./test')
            passed_count = sum(1 for test_case in test_cases if test_case.find('status').get('status') == 'PASS')
            failed_count = sum(1 for test_case in test_cases if test_case.find('status').get('status') == 'FAIL')
            skipped_count = sum(1 for test_case in test_cases if test_case.find('status').get('status') == 'SKIP')
        
            failed_test_cases = []
            error_messages = []
            for test_case in test_cases:
                if test_case.find('status').get('status') == 'FAIL':
                    failed_test_cases.append(test_case.get('name'))
                    # error_msg = test_case.find('.//msg[@level="FAIL"]').text
                    # error_messages.append(error_msg)
        
            suite_data.append({
                'suite_name': suite_name,
                'total_count': passed_count + failed_count + skipped_count,
                'passed_count': passed_count,
                'failed_count': failed_count,
                'skipped_count': skipped_count,
                'failed_test_cases': failed_test_cases,
                'error_messages': error_messages
            })

        return suite_data
    

    def send_Cluster_build_result_notification_to_teams(self, webhook_url, html_file_path, job_name, build_url):
        with open(html_file_path, 'r') as file:
            html_content = file.read()

        payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0078D7",
            "summary": "Jenkins-SWIFT Build Result",
            "sections": [
                {
                    "activityTitle": f"{job_name} Result",
                    "text": html_content
                }              
            ],
            "potentialAction": [
                {
                "@type": "OpenUri",
                "name": "View Job",
                "targets": [{
                    "os": "default",
                    "uri": f"{build_url}"
                }]              
            }]
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))                                                                                                    
        if response.status_code == 200:
            print("Build automation result report sent successfully to Teams.")
        else:
            print(f"Failed to send report. Status Code: {response.status_code}, Response: {response.text}")