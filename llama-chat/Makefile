# Specify the target file to be downloaded
MODEL_URL = https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/resolve/main/mixtral-8x7b-instruct-v0.1.Q2_K.gguf
MODEL_FILE = models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf

# Default target to download the model
all: download

# Rule to download the file using wget
download:
	wget $(MODEL_URL) -O $(MODEL_FILE)

# Clean up downloaded model file
clean:
	rm -f $(MODEL_FILE)

# Phony targets
.PHONY: all download clean