num = input()
method = input()
res = ""
res += "import pytest\n"
res += f"from solutions.sol_{num} import Solution\n\n\n"

params = set()

with open("test_case.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    res += "cases = [\n"
    while line:
        if line.startswith("Example"):
            res += "    {\n"
        elif line.startswith("Input: "):
            res += '        "input": {\n'
            case_input = '            "' + line[7:]
            if case_input[-1] == "\n":
                case_input = case_input[:-1]
            case_input = case_input.replace("null", "None")
            case_input = case_input.replace(" = ", ": ")
            case_input = case_input.replace(", ", ', "')
            case_input = case_input.replace(": ", '": ')
            case_input = case_input.replace(", ", ",")
            case_input = case_input.replace(",", ", ")
            for p in line[7:].split(", "):
                if "=" in p:
                    params.add(p.split(" = ")[0])
            res += case_input + "\n"
            res += "        },\n"
        elif line.startswith("Output: "):
            case_output = line[8:]
            if case_output[-1] == "\n":
                case_output = case_output[:-1]
            case_output = case_output.replace("null", "None")
            case_output = case_output.replace(",", ", ")
            res += f'        "output": {case_output},\n'
            res += "    },\n"
        else:
            pass
        line = file.readline()
    res += "]\n\n\n"

res += f"@pytest.mark.sol{num}\n"
res += "def test_run():\n"
res += "    for case in cases:\n"
res += "        assert (\n"
res += f"            Solution.{method}(\n"
for param in params:
    res += f'                {param}=case["input"]["{param}"],\n'
res += "            )\n"
res += '            == case["output"]\n'
res += "        )\n"


with open(f"../test_solutions/test_{num}.py", "w") as file:
    file.write(res)
