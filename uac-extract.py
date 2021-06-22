#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	print("[!] Specify the UAC value (decimal)")
	sys.exit(1)

controls = {"0x00000001":{"SCRIPT":"The logon script is executed."},
"0x00000002":{"ACCOUNTDISABLE":"The user account is disabled."},
"0x00000008":{"HOMEDIR_REQUIRED":"The home directory is required."},
"0x00000010":{"LOCKOUT":"The account is currently locked out."},
"0x00000020":{"PASSWD_NOTREQD":"No password is required."},
"0x00000040":{"PASSWD_CANT_CHANGE":"The user cannot change the password."},
"0x00000080":{"ENCRYPTED_TEXT_PASSWORD_ALLOWED":"The user can send an encrypted password."},
"0x00000100":{"TEMP_DUPLICATE_ACCOUNT":"This is an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. Also known as a local user account."},
"0x00000200":{"NORMAL_ACCOUNT":"This is a default account type that represents a typical user."},
"0x00000800":{"INTERDOMAIN_TRUST_ACCOUNT":"This is a permit to trust account for a system domain that trusts other domains."},
"0x00001000":{"WORKSTATION_TRUST_ACCOUNT":"This is a computer account for a computer that is a member of this domain."},
"0x00002000":{"SERVER_TRUST_ACCOUNT":"This is a computer account for a system backup domain controller that is a member of this domain."},
"0x00010000":{"DONT_EXPIRE_PASSWD":"The password for this account will never expire."},
"0x00020000":{"MNS_LOGON_ACCOUNT":"This is an MNS logon account."},
"0x00040000":{"SMARTCARD_REQUIRED":"The user must log on using a smart card."},
"0x00080000":{"TRUSTED_FOR_DELEGATION":"The service account (user or computer account), under which a service runs, is trusted for Kerberos delegation. Any such service can impersonate a client requesting the service."},
"0x00100000":{"NOT_DELEGATED":"The security context of the user will not be delegated to a service even if the service account is set as trusted for Kerberos delegation."},
"0x00200000":{"USE_DES_KEY_ONLY":"Restrict this principal to use only Data Encryption Standard (DES) encryption types for keys."},
"0x00400000":{"DONT_REQUIRE_PREAUTH":"This account does not require Kerberos pre-authentication for logon."},
"0x00800000":{"PASSWORD_EXPIRED":"The user password has expired. This flag is created by the system using data from the Pwd-Last-Set attribute and the domain policy."},
"0x01000000":{"TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION:The,account":"is enabled for delegation. This is a security-sensitive setting; accounts with this option enabled should be strictly controlled. This setting enables a service running under the account to assume a client identity and authenticate as that user to other remote servers on the network."},
"0x04000000":{"PARTIAL_SECRETS_ACCOUNT","The account is a read-only domain controller (RODC). It's a security-sensitive setting. Removing this setting from an RODC compromises security on that server."}}

uac = sys.argv[1]
pad = 40 
print(f'{"Name":<{pad}} {"Value":20} {"Description":}')
print(f'{"---------":<{pad}} {"----------":20} {"----------":}')
for i in controls.keys():
    if int(i, 16) & int(uac):
        for k,v in controls.get(i).items():
            value = i+ " (" + str(int(i,16)) + ")"
            print(f'{k:<{pad}} {value:20} {v}')

