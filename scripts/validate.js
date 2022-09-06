console.log('VALIDATE 3');
console.log(process.env);

const addedFiles = process.env.ADDED_FILES ? process.env.ADDED_FILES.split(',') : [];
const modifiedFiles = process.env.MODIFIED_FILES ? process.env.MODIFIED_FILES.split(',') : [];

console.log('addedFiles', addedFiles);
console.log('modifiedFiles', modifiedFiles);

// Get the pattern file....