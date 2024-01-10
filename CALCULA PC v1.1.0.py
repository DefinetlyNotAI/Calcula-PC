# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# And Dont worry I give permission to use this IF you give credit


import re
import time

# Explanation dictionary
explanations = {
    0xC00D07F7: "This object has already been initialized; the setting cannot be changed.",
    0xC00D0802: "One or more data descriptors are not properly set.",
    0xC00D080D: "The given data unit is corrupted, badly formatted, or otherwise not valid.",
    0xC00D07F7: "This object has already been initialized; the setting cannot be changed.",
    0xC00D0802: "One or more data descriptors are not properly set.",
    0xC00D080D: "The given data unit is corrupted, badly formatted, or otherwise not valid.",
    0xC00D0803: "The index has an invalid time interval (probably zero).",
    0xC00D07D2: "The language ID was not found.",
    0xC00D0807: "The specified media type does not work with this component.",
    0xC00D07D0: "An attempt was made to seek or position past the end of a buffer.",
    0xC00D07D1: "The supplied input or output buffer was too small.",
    0xC00D080C: "The object has exceeded its maximum size.",
    0xC00D080E: "The ASF header has exceeded the specified maximum size.",
    0xC00D080A: "The index entries for the specified index block have been unloaded from memory and are not available.",
    0xC00D0801: "The flags for this object or set of objects have not been properly set.",
    0xC00D07E2: "The ASF file header does not contain enough information.",
    0xC00D0805: "The given index value is not valid.",
    0xC00D07F8: "This object has not been initialized properly; that operation cannot be performed.",
    0xC00D07F5: "The request is not valid in the object's current state.",
    0xC00D0804: "The given time value is not valid.",
    0xC00D07E6: "The object does not have a valid clock object.",
    0xC00D07FA: "The ASF Data object could not be found.",
    0xC00D07FD: "The File Properties object could not be found.",
    0xC00D07F9: "The ASF Header object could not be found.",
    0xC00D07FB: "The ASF Index object could not be found.",
    0xC00D07F6: "This object does not have a valid library pointer; it was not properly created or it has been shut down.",
    0xC00D07DB: "The multiple payload packet is missing the payload length.",
    0xC00D07FC: "A Stream Properties object with the correct stream number could not be found.",
    0xC00D080B: "The specified bandwidth is not large enough.",
    0xC00D0809: "The specified data unit requires a larger number of descriptors before it can be fully parsed.",
    0xC00D07F0: "The object was not found.",
    0xC00D07F3: "The object is too large to be processed in the requested manner.",
    0xC00D07ED: "An attempt was made to restore or access an opaque packet.",
    0xC00D07EF: "An attempt was made to store a value which was larger than the destination's maximum value.",
    0xC00D07DE: "The packet content is too large.",
    0xC00D07F7: "This object has already been initialized; the setting cannot be changed.",
    0xC00D0802: "One or more data descriptors are not properly set.",
    0xC00D080D: "The given data unit is corrupted, badly formatted, or otherwise not valid.",
    0xC00D0803: "The index has an invalid time interval (probably zero).",
    0xC00D07D2: "The language ID was not found.",
    0xC00D0807: "The specified media type does not work with this component.",
    0xC00D07D0: "An attempt was made to seek or position past the end of a buffer.",
    0xC00D07D1: "The supplied input or output buffer was too small.",
    0xC00D080C: "The object has exceeded its maximum size.",
    0xC00D080E: "The ASF header has exceeded the specified maximum size.",
    0xC00D080A: "The index entries for the specified index block have been unloaded from memory and are not available.",
    0xC00D0801: "The flags for this object or set of objects have not been properly set.",
    0xC00D07E2: "The ASF file header does not contain enough information.",
    0xC00D0805: "The given index value is not valid.",
    0xC00D07F8: "This object has not been initialized properly; that operation cannot be performed.",
    0xC00D07F5: "The request is not valid in the object's current state.",
    0xC00D0804: "The given time value is not valid.",
    0xC00D07E6: "The object does not have a valid clock object.",
    0xC00D07FA: "The ASF Data object could not be found.",
    0xC00D07FD: "The File Properties object could not be found.",
    0xC00D07F9: "The ASF Header object could not be found.",
    0xC00D07FB: "The ASF Index object could not be found.",
    0xC00D07F6: "This object does not have a valid library pointer; it was not properly created or it has been shut down.",
    0xC00D07DB: "The multiple payload packet is missing the payload length.",
    0xC00D07FC: "A Stream Properties object with the correct stream number could not be found.",
    0xC00D080B: "The specified bandwidth is not large enough.",
    0xC00D0809: "The specified data unit requires a larger number of descriptors before it can be fully parsed.",
    0xC00D07F0: "The object was not found.",
    0xC00D07F3: "The object is too large to be processed in the requested manner.",
    0xC00D07ED: "An attempt was made to restore or access an opaque packet.",
    0xC00D07EF: "An attempt was made to store a value which was larger than the destination's maximum value.",
    0xC00D07DE: "The packet content is too large.",
    0xC00D2711: "A problem has occurred in the Digital Rights Management component. Contact product support for this application.",
    0xC00D2712: "License storage is not working. Contact Microsoft product support.",
    0xC00D2713: "Secure storage is not working. Contact Microsoft product support.",
    0xC00D2714: "License acquisition did not work. Acquire a new license or contact the content provider for further assistance.",
    0xC00D2715: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2716: "The media file is corrupted. Contact the content provider to get a new file.",
    0xC00D2717: "The license is corrupted. Acquire a new license.",
    0xC00D2718: "The license is corrupted or invalid. Acquire a new license.",
    0xC00D2719: "Licenses cannot be copied from one computer to another. Use License Management to transfer licenses, or get a new license for the media file.",
    0xC00D271B: "License storage is not working. Contact Microsoft product support.",
    0xC00D271C: "The media file is corrupted. Contact the content provider to get a new file.",
    0xC00D271D: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D271E: "The license could not be acquired. Try again later.",
    0xC00D271F: "License acquisition did not work. Acquire a new license or contact the content provider for further assistance.",
    0xC00D2720: "The requested operation cannot be performed on this file.",
    0xC00D2721: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2722: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2723: "The media file is corrupted. Contact the content provider to get a new file.",
    0xC00D2725: "The license is corrupted. Acquire a new license.",
    0x000D2726: "The license was acquired.",
    0x000D2727: "The security upgrade has been completed.",
    0xC00D2728: "A security upgrade is required to perform the operation on this media file.",
    0xC00D2729: "You already have the latest security components. No upgrade is necessary at this time.",
    0xC00D272A: "The application cannot perform this action. Contact product support for this application.",
    0xC00D272B: "You cannot begin a new license acquisition process until the current one has been completed.",
    0xC00D272C: "You cannot begin a new security upgrade until the current one has been completed.",
    0xC00D272D: "Failure to restore backup.",
    0xC00D272E: "Bad request ID to restore backup.",
    0xC00D272F: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2730: "A license cannot be created for this media file. Reinstall the application.",
    0xC00D2731: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2732: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2733: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2734: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2735: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2736: "The security upgrade failed. Try again later.",
    0xC00D2737: "License storage is not working. Contact Microsoft product support.",
    0xC00D2738: "License storage is not working. Contact Microsoft product support.",
    0xC00D2739: "License storage is not working. Contact Microsoft product support.",
    0xC00D273A: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D273B: "A problem has occurred in the Digital Rights Management component. Contact product support for this application.",
    0xC00D273C: "License storage is not working. Contact Microsoft product support.",
    0xC00D273D: "The media file is corrupted. Contact the content provider to get a new file.",
    0xC00D273E: "A problem has occurred in the Digital Rights Management component. Try again later.",
    0xC00D273F: "The application has made an invalid call to the Digital Rights Management component. Contact product support for this application.",
    0xC00D2740: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2741: "A problem has occurred in the Digital Rights Management component. Contact product support for this application.",
    0xC00D2742: "Licenses are already backed up in this location.",
    0xC00D2743: "One or more backed-up licenses are missing or corrupt.",
    0xC00D2744: "You cannot begin a new backup process until the current process has been completed.",
    0xC00D2745: "Bad data sent to restore backup request.",
    0x000D2746: "Status message: License monitoring has been cancelled.",
    0x000D2747: "Status message: License acquisition has been cancelled.",
    0xC00D2748: "The license is invalid. Contact the content provider for further assistance.",
    0xC00D2749: "A required property was not set by the application. Contact product support for this application.",
    0xC00D274A: "A problem has occurred in the Digital Rights Management component of this application. Try to acquire a license again.",
    0xC00D274B: "A license cannot be found for this media file. Use License Management to transfer a license for this file from the original computer, or acquire a new license.",
    0xC00D274C: "A problem occurred during the security upgrade. Try again later.",
    0xC00D274D: "Certified driver components are required to play this media file. Contact Windows Update to see whether updated drivers are available for your hardware.",
    0xC00D274E: "One or more of the Secure Audio Path components were not found or an entry point in those components was not found.",
    0xC00D274F: "Status message: Reopen the file.",
    0xC00D2750: "Certain driver functionality is required to play this media file. Contact Windows Update to see whether updated drivers are available for your hardware.",
    0xC00D2751: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2752: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2753: "You cannot restore your license(s).",
    0xC00D2754: "The licenses for your media files are corrupted. Contact Microsoft product support.",
    0xC00D2755: "To transfer this media file, you must upgrade the application.",
    0xC00D2756: "You cannot make any more copies of this media file.",
    0xC00D2757: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2758: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2759: "Unable to obtain license.",
    0xC00D275A: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D275B: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D275C: "The buffer supplied is not sufficient.",
    0xC00D275D: "The property requested is not supported.",
    0xC00D275E: "The specified server cannot perform the requested operation.",
    0xC00D275F: "Some of the licenses could not be stored.",
    0xC00D2760: "The Digital Rights Management security upgrade component could not be validated. Contact Microsoft product support.",
    0xC00D2761: "Invalid or corrupt data was encountered.",
    0xC00D2762: "The Windows Media Digital Rights Management system cannot perform the requested action because your computer or network administrator has enabled the group policy preventing Windows Media DRM Internet access.",
    0xC00D2763: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D2764: "Not all of the necessary properties for DRM have been set.",
    0xC00D2765: "The portable device does not have the security required to copy protected files to it. To obtain the additional security, try to copy the file to your portable device again. When a message appears, click OK.",
    0xC00D2766: "Too many resets occurred during restore operation.",
    0xC00D2767: "Running this process under a debugger while using DRM content is not allowed.",
    0xC00D2768: "The user canceled the DRM operation.",
    0xC00D2769: "The license you are using has output restrictions. This license is unusable until these restrictions are queried.",
    0xC00D276A: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D276B: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D276C: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0xC00D276D: "A problem has occurred in the Digital Rights Management component. Contact Microsoft product support.",
    0x000D276E: "The track can be copied and has no playlist burn limit.",
    0x000D276F: "The track can be copied and has a playlist burn limit.",
    0xC00D2770: "The specified track has exceeded its specified playlist burn limit in this playlist.",


}


# Functions

# RLE encoder
def run_length_encode(input_string):
    pattern = re.compile(r'((\w)\2*)')
    result = pattern.findall(input_string)
    encoded_string = ""
    for match, char in result:
        if len(match) > 1:
            encoded_string += str(len(match)) + "(" + char + ")"
        else:
            encoded_string += char
    return encoded_string

# RLE decoder
def run_length_decode(encoded_string):
    decoded_string = ""
    pattern = re.compile(r'(\d+)?\((\w*)\)|(\w)')
    matches = pattern.findall(encoded_string)
    for match in matches:
        if match[0]:
            count = int(match[0])
            char = match[1]
            decoded_string += count * char
        elif match[2]:
            decoded_string += match[2]
    return decoded_string

# Integer to Binary Calculator
def int_to_binary(num):
    if not num:
        return "Error: Please enter a non-empty value"
    if not isinstance(num, int):
        return "Error: Please enter an integer"
    if num < 0:
        return "Error: Please enter a non-negative number"
    
    binary_representation = bin(num)[2:]
    bit_length = len(binary_representation)
    
    if bit_length > 128:
        return "Buffer Overflow: Binary representation exceeds 128 bits"
    
    padded_binary = binary_representation.zfill(128)
    spaced_binary = ' '.join(padded_binary[i:i+4] for i in range(0, len(padded_binary), 4))
    return spaced_binary

# The Memory Calculator
def kb_to_kib(kb):
    return round(kb * 0.9765625, 2)
def mb_to_mib(mb):
    return round(mb * 0.95367431640625, 2)
def gb_to_gib(gb):
    return round(gb * 0.9313225746154785, 2)
def tb_to_tib(tb):
    return round(tb * 0.9094947017729282, 2)

# Decimal to Hexadecimal
def decimal_to_hexadecimal():
    try:
        decimal_number = int(input("Enter a decimal number: "))
        hexadecimal_number = hex(decimal_number)
        return hexadecimal_number
    except ValueError:
        return "Error: Please enter a valid decimal number"

def boolean_calculator():
   print("\nChoose operation:")
   print("1. AND")
   print("2. OR")
   print("3. NOT")
   print("4. NOR")
   print("5. NAND")
   print("6. XOR")
   print("7. CMPX")
   choice = input()

   if choice == '7':
       return "This feature is being implemented"

   print("Enter first value (0 or 1):")
   val1 = int(input())

   print("Enter second value (0 or 1):")
   val2 = int(input())

   if choice == '1':
       result = val1 & val2
   elif choice == '2':
       result = val1 | val2
   elif choice == '3':
       result = ~val1 & val2
   elif choice == '4':
       result = ~(val1 | val2)
   elif choice == '5':
       result = ~(val1 & val2)
   elif choice == '6':
       result = val1 ^ val2

   return "The resultant value is" , result

# Binary Calculator
def binary_addition(num1, num2):
    return bin(int(num1, 2) + int(num2, 2))[2:].zfill(8)
def binary_subtraction(num1, num2):
    return bin(int(num1, 2) - int(num2, 2))[2:].zfill(8)
def binary_multiplication(num1, num2):
    return bin(int(num1, 2) * int(num2, 2))[2:].zfill(8)
def binary_division(num1, num2):
    try:
        result = int(num1, 2) // int(num2, 2)
        return bin(result)[2:].zfill(8)
    except ZeroDivisionError:
        return "Error: Division by zero"
def validate_binary_input(binary_num):
    if all(bit in '01' for bit in binary_num) and len(binary_num) == 8:
        return True
    else:
        return False
# Windows Error Explainer for Hexadecimal        
def explain_error(hexadecimal_err_code):
    try:
        decimal_err_code = int(hexadecimal_err_code, 16)
        if decimal_err_code in explanations:
            return explanations[decimal_err_code]
        else:
            return "The provided hexadecimal error code is unknown. Please refer to the documentation or contact support for further assistance."
    except ValueError:
        return "Error: Invalid hexadecimal error code."

# Main Menu, Oooh ASCII ART, Definetly not made from a website ;) 
def main_menu():
    print(r"_________     _____  .____   _________  ____ ___.____       _____    ___________________ ")
    print(r"\_   ___ \   /  _  \ |    |  \_   ___ \|    |   \    |     /  _  \   \______   \_   ___ \ ")
    print(r"/    \  \/  /  /_\  \|    |  /    \  \/|    |   /    |    /  /_\  \   |     ___/    \  \/ ")
    print(r"\     \____/    |    \    |__\     \___|    |  /|    |___/    |    \  |    |   \     \____")
    print(r" \______  /\____|__  /_______ \______  /______/ |_______ \____|__  /  |____|    \______  /")
    print(r"        \/         \/        \/      \/                 \/       \/                    \/ ")
    print("")
    print("V1.0")
    print("")
    print("Note this is made by a child, so please don't take this seriously, Coded in Python, Simple Calculator-Like Functions")
    print("You may use this in any way you want, You may modify the code, just please add credit")
    print("Enjoy Calcula PC and if you find bugs please tell me, I would add you to the credits")
    print("\nTested on Windows")
    print("")
    
    
    
    
    
    while True: # Forever Loop
    
        # Calculator Menu
        print("\nCalculator Menu:")
        print("1. Binary Operations")
        print("2. Decimal to Hexadecimal")
        print("3. Unit Conversion")
        print("4. Windows Error Explainer")
        print("5. Number to Binary")
        print("6. RLE")
        print("7. Boolean Calculator")
        print("99. Exit")
        print("\n")
        choice = input("Enter your choice (1/2/3/4/5/6/7/99): ")

        
        if choice == '99':
            print("Exiting the program. Goodbye!")
            time.sleep(2)
            break
            
        # Binary Calculator
        if choice == '1':
            #Binary Calc's Menu
            print("Binary Calculator Menu:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            operation_choice = input("Enter your choice (1/2/3/4): ")
               
            # In Calc Menu
            if operation_choice in ['1', '2', '3', '4']:
                num1 = input("Enter the first 8-bit binary number: ")
                num2 = input("Enter the second 8-bit binary number: ")
                
                # Error System and Calculator
                if validate_binary_input(num1) and validate_binary_input(num2):
                    if operation_choice == '1':
                        print("Result: ", binary_addition(num1, num2))
                    elif operation_choice == '2':
                        print("Result: ", binary_subtraction(num1, num2))
                    elif operation_choice == '3':
                        print("Result: ", binary_multiplication(num1, num2))
                    elif operation_choice == '4' and num2 != '00000000':
                        print("Result: ", binary_division(num1, num2))
                    else:
                        print("Error: Division by zero or invalid input")
                else:
                    print("Error: Please enter valid 8-bit binary numbers")
            else:
                print("Invalid operation choice. Please enter a number between 1 and 4.")
        
        # Decimal to Hexadecimal Calculator (Links To a previous function)
        elif choice == '2':
            print(decimal_to_hexadecimal())

        # Storage Convertor 
        elif choice == '3':
            # Menu System
            print("Unit Conversion Menu:")
            print("1. Kilobyte (KB) to Kibibyte (KiB)")
            print("2. Megabyte (MB) to Mebibyte (MiB)")
            print("3. Gigabyte (GB) to Gibibyte (GiB)")
            print("4. Terabyte (TB) to Tebibyte (TiB)")
            
            # Calculations Area - Links to previous functions
            unit_choice = int(input("Enter your choice (1-4): "))
            if unit_choice in [1, 2, 3, 4]:
                if unit_choice == 1:
                    kb = float(input("Enter the size in Kilobytes (KB): "))
                    kib = kb_to_kib(kb)
                    print(f"~{kb} KB is approximately equal to ~{kib} KiB")
                elif unit_choice == 2:
                    mb = float(input("Enter the size in Megabytes (MB): "))
                    mib = mb_to_mib(mb)
                    print(f"~{mb} MB is approximately equal to ~{mib} MiB")
                elif unit_choice == 3:
                    gb = float(input("Enter the size in Gigabytes (GB): "))
                    gib = gb_to_gib(gb)
                    print(f"~{gb} GB is approximately equal to ~{gib} GiB")
                elif unit_choice == 4:
                    tb = float(input("Enter the size in Terabytes (TB): "))
                    tib = tb_to_tib(tb)
                    print(f"~{tb} TB is approximately equal to ~{tib} TiB")
            else: # Error System to prevent Crashes
                print("Invalid choice. Please enter a number between 1 and 4.")
                
        # Windows Hexadecimal Error Explainer - Uses Previous explanation's - Taken from Windows        
        elif choice == '4':
            user_input = input("Enter a hexadecimal error code: ")
            explanation = explain_error(user_input)
            print(explanation)
        elif choice == '5':
            # Error System
            try:
                user_input = input("Number? ")
                if user_input:
                    integer = int(user_input)
                    print(int_to_binary(integer))
                else:
                    print("Error: Please enter a non-empty value")
            except ValueError:
                print("Error: Please enter an integer")        
                
                
        # RLE       
        elif choice == '6':
        
            action = input("Enter 'encode' to encode a string, 'decode' to decode a string, or 'exit' to quit: ")
            if action.lower() == "exit":
                break
            elif action.lower() == "encode":
                input_string = input("Enter a string to encode: ")
                if not input_string.strip():
                    print("Error: Input cannot be empty. Please enter a valid string.")
                elif any(char in input_string for char in ['@', '$', '?', '-']):
                    print("Error: Input string contains special characters. Please enter a valid string.")
                else:
                    encoded_string = run_length_encode(input_string)
                    original_length = len(input_string)
                    encoded_length = len(encoded_string)
                    optimization_percentage = ((original_length - encoded_length) / original_length) * 100
                    if optimization_percentage <= 0:
                        print("Optimization percentage is less than or equal to 0. Reprinting the input string.")
                        print("Input string:", input_string)
                    else:
                        print("Encoded string:", encoded_string)
                        optimization_percentage = round(optimization_percentage)
                        print("Optimization percentage:", optimization_percentage, "%")
            # Error Detection
            elif action.lower() == "decode":
                encoded_string = input("Enter a string to decode: ")
                decoded_string = run_length_decode(encoded_string)
                print("Decoded string:", decoded_string)
            else:
                print("Invalid action. Please enter 'encode', 'decode', or 'exit'.")        
        
        elif choice == '7':
            print boolean_calculator()
        
        # Main Menu Error Response
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 99.")

#Finalized Code
main_menu()
