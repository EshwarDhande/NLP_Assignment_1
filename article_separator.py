import os

def split_text_files(input_dirs, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    name = 0
    # Iterate through each input directory
    for input_dir in input_dirs:
        for root, _, files in os.walk(input_dir):
            for filename in files:
                if filename.endswith(".txt"):
                    input_file_path = os.path.join(root, filename)
                    with open(input_file_path, "r") as input_file:
                        content = input_file.read()

                    # Split content by newline character
                    lines = content.split("\n")

                    # Save smaller text files in the output directory
                    for line in lines:
                        output_file_path = os.path.join(output_dir, f"{name}_.txt")
                        with open(output_file_path, "w") as output_file:
                                output_file.write(line)
                        name += 1
                        print(f"{name}.txt done")
        print(input_dir)

if __name__ == "__main__":
 
    input_dirs=['/mnt/HDFS1/llm/llmmarathi/Pendse/sangrah','/mnt/HDFS1/llm/llmmarathi/Pendse/sangrah1','/mnt/HDFS1/llm/llmmarathi/Pendse/sangrah2']
    
    output_dir = "/mnt/HDFS1/llm/llmmarathi/Pendse/sangrah_separated_final"  # Output directory
    split_text_files(input_dirs, output_dir)
