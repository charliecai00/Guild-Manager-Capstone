This is a collection of example API calls. <br>
Each file is named [Call Name]_[type], where the type is either INPUT or OUTPUT. <br>
INPUT: json sent by the client to the server <br>
OUTPUT: json sent by the server to the client <br>
There is the Base_Input.json, which is the body of the json always sent by the client <br>
 - It has two fields: <br>
    - "Type" is just the name of the command, the same as the example json file
    - "Data" is the contents of the actual command json
- If a command is missing an OUTPUT or INPUT example, that means it does not have OUTPUT or INPUT
    - For example, Hire_Heroes does not have an OUTPUT json (only an INPUT). This is because that command does not return any game data back the client (it can still return non game data if you want it to ofc)