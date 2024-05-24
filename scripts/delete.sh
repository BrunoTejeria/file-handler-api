if [ -d "../uploads/" ]; then
    find ../uploads -type f -name "*.txt" -delete
else
    echo 'Folder "uploads" not found.'
fi