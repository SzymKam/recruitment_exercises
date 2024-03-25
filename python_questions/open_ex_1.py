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
                case_result = line.split('- ')[1].strip()
                test_cases[case_id]["status"] = case_result

            elif '  (sec)   End:' in line:
                duration = line.split(' ')[0]
                test_cases[case_id]["duration"] = int(duration)

        passed_tests = len([test for test in test_cases.values() if test["status"] == "passed"])
        failed_tests = len([test for test in test_cases.values() if test["status"] == "failed"])
        success_rate = (passed_tests / (passed_tests + failed_tests)) * 100

        print(f"Number of failed tests: {failed_tests}")
        print(f"Number of failed tests: {passed_tests}")
        print(f"Success rate: {success_rate}%")

        sorted_test_cases = sorted(test_cases.items(), key=lambda x: x[1]["duration"], reverse=True)[:3]

        print(f"3 TestCasesID with longest duration time:")
        for test in sorted_test_cases:
            print(f"* {test[0]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <script_name.py> <jenkins_log_file.txt>")
        sys.exit(1)

    work_with_logs(sys.argv)
