# ClonePhish.py

`ClonePhish.py` is a Python tool for cloning websites and setting up a local phishing server. It clones a specified website, modifies it to collect credentials and system information, and serves it locally to capture data from visitors.

## Features

- **Website Cloning:** Fetches and saves the HTML of a given website.
- **Phishing Capabilities:** Alters forms to submit data to the local server.
- **System Information Collection:** Collects user system information such as User-Agent, screen resolution, timezone, and language.
- **Credential Logging:** Captures and logs credentials submitted via the cloned forms.
- **IP Address Logging:** Logs the IP address of visitors.

## Requirements

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `colorama`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 colorama
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/0xgh057r3c0n/ClonePhish.git
   cd ClonePhish
   ```

2. **Run the Tool:**

   ```bash
   python3 ClonePhish.py -d <target-url>
   ```

   Replace `<target-url>` with the URL of the website you want to clone. For example:

   ```bash
   python3 ClonePhish.py -d https://example.com
   ```

3. **Access the Local Server:**

   After running the tool, it will start a local server. You can access it by navigating to `http://<local-ip>:8080` in your web browser.

## How It Works

- **Fetching HTML:** The tool fetches the HTML content of the specified URL.
- **Modifying HTML:** It modifies form actions and injects JavaScript to collect system information.
- **Starting the Server:** Hosts the modified HTML locally and listens for incoming requests to capture credentials and system information.

## Ethical Considerations

**WARNING:** This tool is intended for educational purposes and should only be used in environments where you have explicit permission to conduct security testing or phishing simulations. Unauthorized use of this tool is illegal and unethical.

## License

This tool is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please contact [gauravbhattacharjee54@gmail.com](mailto:gauravbhattacharjee54@gmail.com).

**Disclaimer:** The creator of this tool assumes no responsibility for its misuse. Use it responsibly and only in legal and ethical contexts.
