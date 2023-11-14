#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

// Read the content of fileA
const fileAContent = fs.readFileSync(fileAPath, 'utf-8');

// Read the content of fileB
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');

// Concatenate the contents of fileA and fileB
const concatenatedContent = `${fileAContent}${fileBContent}`;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationPath, concatenatedContent);

console.log(`Concatenation complete. Result saved to ${destinationPath}`);
