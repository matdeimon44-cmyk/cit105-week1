# PuTTY SSH Connection Runbook

## Purpose

This runbook explains how to connect to a remote server from a Windows computer using PuTTY and SSH key authentication. It is written so that a user with no previous experience can follow the steps from start to finish.

## What You Need Before Starting

Before beginning, make sure you have:

- A Windows computer.
- PuTTY installed.
- PuTTYgen installed.
- The SSH key file provided for the server.
- The server IP address.
- The username used to connect to the server.

Keep the SSH key file in a safe location on your computer. Never upload a private key to GitHub or share it with another person.
## Convert the SSH Key with PuTTYgen

1. Open PuTTYgen on the Windows computer.
2. Click **Load**.
3. Select the original SSH private key file provided for the server.
4. If the key file does not appear, change the file type filter to **All Files (*.*)**.
5. After the key loads successfully, click **Save private key**.
6. Save the converted key with a `.ppk` extension.
7. Store the `.ppk` file in a safe folder on the computer.

The original key should be kept as a backup. PuTTY uses the `.ppk` file for authentication.

## Configure PuTTY

1. Open PuTTY.
2. In **Host Name (or IP address)**, enter the server IP address.
3. Set the **Port** to `22`.
4. Select **SSH** as the connection type.
5. In the left menu, go to **Connection > Data**.
6. Enter the username for the server in **Auto-login username**.
7. Go to **Connection > SSH > Auth > Credentials**.
8. Click **Browse** next to the private key field.
9. Select the `.ppk` file created with PuTTYgen.
10. Return to **Session**.
11. Enter a name in **Saved Sessions**.
12. Click **Save**.

The saved session allows the same connection settings to be reused without entering every setting again.

## Connect to the Server

1. Select the saved PuTTY session.
2. Click **Open**.
3. On the first connection, PuTTY may display a host key security warning.
4. Verify that you are connecting to the expected server and accept the host key only if the server information is correct.
5. After accepting it, PuTTY stores the host key so the same warning should not normally appear again for that server.
6. If authentication succeeds, a terminal window opens and the server shell prompt appears.

A successful connection means the SSH session is active and commands can now be entered on the remote server.

## Troubleshooting

### 1. Connection Timed Out

**Message:** `Network error: Connection timed out`

**Meaning:** PuTTY could not reach the server.

**First checks:**
- Verify the server IP address.
- Verify that the computer has an Internet connection.
- Confirm that port 22 is allowed.
- Confirm that the server is running.

### 2. Connection Refused

**Message:** `Network error: Connection refused`

**Meaning:** The server was reached, but the SSH service did not accept the connection.

**First checks:**
- Verify that port 22 is correct.
- Confirm that the SSH service is running on the server.
- Confirm that firewall rules allow SSH connections.

### 3. Authentication Failed

**Message:** `No supported authentication methods available`

or

`Server refused our key`

**Meaning:** The server did not accept the SSH key used for authentication.

**First checks:**
- Confirm that the correct `.ppk` file was selected.
- Confirm that the correct username was entered.
- Confirm that the public key installed on the server matches the private key being used.

### 4. Wrong Username

**Message:** `Access denied`

**Meaning:** The username or authentication information is incorrect.

**First checks:**
- Verify the username provided for the server.
- Verify that the correct private key is selected.
- Reload the saved PuTTY session and try again.

## SSH Key Security

The private SSH key must be protected.

- The private key must not be uploaded to GitHub.
- The `.ppk` private key must not be shared with another person.
- The public key may be copied to systems that need to allow authentication.
- Do not include the contents of a key, key fingerprint, or screenshots showing key material in this repository.
- If a private key is exposed, it should be considered compromised and replaced with a new key pair.

## Final Test

To verify this runbook:

1. Close PuTTY completely.
2. Delete or ignore the previously saved PuTTY session.
3. Start again from the beginning of this document.
4. Load the correct key.
5. Configure the IP address, port, username, and private key.
6. Save the PuTTY session.
7. Open the connection.
8. Confirm that the remote shell prompt appears successfully.

If the connection works without needing information that is not written in this document, the runbook is complete.