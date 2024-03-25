"""
Napisać skrypt parsujący logi z Jenkinsa, który:

Pokazuje poniższe dane

Number of passed tests: 75
Number of failed tests: 25
Success rate: 75%

3 TestCasesID with longest duration time:
* TC_CRM_30050 - 300 (s)
* TC_CRM_30051 - 299 (s)
* TC_CRM_30052 - 298 (s)

Dodatkowe info w logach:
$$$ ID|<TestCaseID>|
<Counter> - <status|passed|failed|skipped>
<duration_in_seconds>   (sec)   End:
<tc_endtime>    SCENARIO: <scenario_name>

Uruchomienie skryptu:

python <nazwa_skryptu.py> <plik_txt_z_logami.txt>

"""
import sys


def work_with_logs(logs):

    test_cases = {}

    with open(logs[1], 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('$$$ ID|'):
                case_id = line.split('|')[1]
                test_cases[case_id] = {"status": "", "duration": 0}

            elif ('failed' in line or 'passed' in line or 'skipped' in line) and ' - ' in line:
                case_result = line.split('- ')[1]
                test_cases[case_id]["status"] = case_result

            elif




    print(test_cases)




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <script_name.py> <jenkins_log_file.txt>")
        sys.exit(1)

    work_with_logs(sys.argv)
