import subprocess
import time

java_command = "/home/codespace/java/current/bin/java -Xmx100G -Xms4G -jar /workspaces/sarvesh8456/paper-1.19-81.jar --nogui"

def run_java_command():
    try:
        # Execute the Java command
        subprocess.run(java_command, shell=True)
    except Exception as e:
        print("Error executing Java command:", e)

def print_java_command():
    print(java_command)

def main():
    # Define the interval (4 hours and 10 seconds)
    interval_seconds = 4 * 60 * 60 + 10

    while True:
        # Run the Java command
        run_java_command()

        # Print the Java command
        print_java_command()

        # Sleep for the specified interval
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
