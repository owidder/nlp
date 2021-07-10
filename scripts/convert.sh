find $1 -type f | \
    (while read file; do
        iconv -f ISO-8859-1 -t UTF-8 "$file" > "${file}.tmp";
        rm "$file"
        mv "${file}.tmp" "$file"
    done);