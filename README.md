# ClonePhish

`ClonePhish` is a Python tool designed to clone websites and host them locally for phishing and security research purposes. This tool can capture system information and user inputs, logging them for analysis. 

**Note:** This tool should only be used in a legal and ethical manner. Ensure you have explicit permission to test any website with this tool.

## Features
- Clone a website and serve it locally.
- Capture and log system information (e.g., User-Agent, screen resolution).
- Log user input fields (e.g., email, password) from the cloned forms.
- Redirect users to the original website after form submission.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `colorama`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 colorama
```

## Usage

1. **Clone a Website and Start the Server:**

   Run the script with the `-d` option to specify the domain of the website you want to clone:

   ```bash
   python3 ClonePhish.py -d http://example.com
   ```

2. **Access the Cloned Website:**

   Open a web browser and navigate to the server address printed in the terminal, e.g., `http://192.168.29.95:8080/`.

3. **Monitor Logs:**

   The tool will log captured system information and form data to the terminal and save them to files:
   
   - `stolen_credentials.txt` for user credentials.
   - `system_info.txt` for system information.

## Example Output

**Terminal Output:**

```
[+] Received system info:
   User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0
   Screen Resolution: 1366x768
   Timezone: Asia/Kolkata
   Language: en-US

[+] Received form data:
   email: user@example.com
   password: secret123
```

**Files Created:**

- `stolen_credentials.txt`:
  ```
  Username: user@example.com
  Password: secret123
  ```

- `system_info.txt`:
  ```
  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0
  Screen Resolution: 1366x768
  Timezone: Asia/Kolkata
  Language: en-US
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
