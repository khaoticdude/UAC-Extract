#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	print("[!] Specify the UAC value (decimal)")
	sys.exit(1)

controls = {"0x00000001":{"ADS_UF_SCRIPT":"The logon script is executed."},
"0x00000002":{"ADS_UF_ACCOUNTDISABLE":"The user account is disabled."},
"0x00000008":{"ADS_UF_HOMEDIR_REQUIRED":"The home directory is required."},
"0x00000010":{"ADS_UF_LOCKOUT":"The account is currently locked out."},
"0x00000020":{"ADS_UF_PASSWD_NOTREQD":"No password is required."},
"0x00000040":{"ADS_UF_PASSWD_CANT_CHANGE":"The user cannot change the password."},
"0x00000080":{"ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED":"The user can send an encrypted password."},
"0x00000100":{"ADS_UF_TEMP_DUPLICATE_ACCOUNT":"This is an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. Also known as a local user account."},
"0x00000200":{"ADS_UF_NORMAL_ACCOUNT":"This is a default account type that represents a typical user."},
"0x00000800":{"ADS_UF_INTERDOMAIN_TRUST_ACCOUNT":"This is a permit to trust account for a system domain that trusts other domains."},
"0x00001000":{"ADS_UF_WORKSTATION_TRUST_ACCOUNT":"This is a computer account for a computer that is a member of this domain."},
"0x00002000":{"ADS_UF_SERVER_TRUST_ACCOUNT":"This is a computer account for a system backup domain controller that is a member of this domain."},
"0x00010000":{"ADS_UF_DONT_EXPIRE_PASSWD":"The password for this account will never expire."},
"0x00020000":{"ADS_UF_MNS_LOGON_ACCOUNT":"This is an MNS logon account."},
"0x00040000":{"ADS_UF_SMARTCARD_REQUIRED":"The user must log on using a smart card."},
"0x00080000":{"ADS_UF_TRUSTED_FOR_DELEGATION":"The service account (user or computer account), under which a service runs, is trusted for Kerberos delegation. Any such service can impersonate a client requesting the service."},
"0x00100000":{"ADS_UF_NOT_DELEGATED":"The security context of the user will not be delegated to a service even if the service account is set as trusted for Kerberos delegation."},
"0x00200000":{"ADS_UF_USE_DES_KEY_ONLY":"Restrict this principal to use only Data Encryption Standard (DES) encryption types for keys."},
"0x00400000":{"ADS_UF_DONT_REQUIRE_PREAUTH":"This account does not require Kerberos pre-authentication for logon."},
"0x00800000":{"ADS_UF_PASSWORD_EXPIRED":"The user password has expired. This flag is created by the system using data from the Pwd-Last-Set attribute and the domain policy."},
"0x01000000":{"ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION:The,account":"is enabled for delegation. This is a security-sensitive setting; accounts with this option enabled should be strictly controlled. This setting enables a service running under the account to assume a client identity and authenticate as that user to other remote servers on the network."}}

uac = sys.argv[1]
pad = 40 
print(f'{"Name":<{pad}} {"Value":15} {"Description":}')
print(f'{"---------":<{pad}} {"----------":15} {"----------":}')
for i in controls.keys():
    if int(i, 16) & int(uac):
        for k,v in controls.get(i).items():
            print(f'{k:<{pad}} {i:15} {v}')

