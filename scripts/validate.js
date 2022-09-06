console.log('VALIDATE 3');
console.log(process.env);

const addedFiles = process.env.ADDED_FILES ? process.env.ADDED_FILES.split(',') : [];
const modifiedFiles = process.env.MODIFIED_FILES ? process.env.MODIFIED_FILES.split(',') : [];

console.log('addedFiles', addedFiles);
console.log('modifiedFiles', modifiedFiles);

// Get the pattern file....

// example-pattern.json

const findFile = (array, filename) => array.find(item => item.includes(filename));

const pattern = findFile([...addedFiles, ...modifiedFiles], 'example-pattern.json');

console.log('Pattern', pattern);
console.log('README', findFile([...addedFiles, ...modifiedFiles], 'README.md'));