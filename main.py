import csv
import argparse
import os

def convert_truth_table(input_file, separador):
    """
    Convert a CSV truth table to inputs and outputs in separate blocks,
    skipping the first row (header).
    
    Args:
        input_file (str): Path to input CSV file
        separador (str): Character that separates inputs from outputs
    
    Returns:
        tuple: Lists of input and output strings
    """
    input_strings = []
    output_strings = []
    
    try:
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip the header row
            next(csv_reader)
            #Iterate over the rest
            for row in csv_reader:
                # Find the separador index
                separador_index = row.index(separador)
                # Split inputs and outputs
                inputs = row[:separador_index]
                outputs = row[separador_index + 1:]
                # Concatenate inputs and outputs into strings
                input_string = ''.join(inputs)
                output_string = ''.join(outputs)
                input_strings.append(input_string)
                output_strings.append(output_string)
        
        return input_strings, output_strings
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return None, None
    except ValueError:
        print(f"Error: separador '{separador}' not found in one or more rows.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

def print_results(input_strings, output_strings,codigo):
    """Print the results to console in a formatted way"""
    print("\nRESULTADOS:")
    print("=========")
    print("ENTRADAS:")
    for input_string in input_strings:
        print(input_string)
    
    print("\n=========")
    print("SALIDAS:")
    for output_string in output_strings:
        print(output_string)
    print("=========")
    #Results in VHDL CODE
    print('\n====Resultados formato switch VHDL====\n')
    for input_str, output_str in zip(input_strings, output_strings):
        print(f"when \"{input_str}\" => {codigo} <= \"{output_str}\"")

def save_to_file(input_strings, output_strings, input_file, codigo):
    """Save results to a new txt file in the same directory as the input file"""
    # Create output filename based on input filename
    input_base = os.path.splitext(input_file)[0]
    output_file = f"{input_base}_convertido.txt"
    try:
        with open(output_file, 'w') as txt_file:
            txt_file.write("ENTRADAS:\n")
            #Escribir entradas
            for input_string in input_strings:
                txt_file.write(f"{input_string}\n")
            
            txt_file.write("\nSALIDAS:\n")
            for output_string in output_strings:
                txt_file.write(f"{output_string}\n")
            
            ##Escribir entradas como codigo
            txt_file.write("\n\n=======SWICTH VHDL==========\n")
            for input_str, output_str in zip(input_strings, output_strings):
                txt_file.write(f" when \"{input_str}\" => {codigo} <= \"{output_str}\"\n")
            
        
        print(f"\n\nSalida y codigo guardados en: {output_file}")
        return True
    
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return False

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Convert CSV truth table to blocked binary strings')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('--separador', default='|', help='separador character between inputs and outputs (default: ,)')
    parser.add_argument('--codigo', default='display', help='Nombre de las salidas para la generacion de codigo VHDL')
    args = parser.parse_args()
    
    # Convert the truth table
    input_strings, output_strings = convert_truth_table(args.input_file, args.separador)
    
    if input_strings is not None and output_strings is not None:
        # Print results to console
        print_results(input_strings, output_strings, args.codigo)
        # Save results to file
        save_to_file(input_strings, output_strings, args.input_file, args.codigo)

if __name__ == "__main__":
    main()