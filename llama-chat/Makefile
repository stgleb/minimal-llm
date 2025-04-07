# Specify the target file to be downloaded
MODEL_URL = https://huggingface.co/mradermacher/Mixtral-8x7B-Instruct-v0.1-GGUF/resolve/main/Mixtral-8x7B-Instruct-v0.1.IQ3_M.gguf
MODEL_FILE = models/Mixtral-8x7B-Instruct-v0.1.IQ3_M.gguf

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