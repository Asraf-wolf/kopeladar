const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, 'data');
const eventsDir = path.join(dataDir, 'events');
const outputFile = path.join(dataDir, 'events-index.json');

// 1. Ensure the directories exist so Cloudflare doesn't throw an error
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir);
if (!fs.existsSync(eventsDir)) fs.mkdirSync(eventsDir);

let events = [];
const files = fs.readdirSync(eventsDir).filter(file => file.endsWith('.json'));

// 2. Loop through every event file and grab the data
files.forEach(file => {
    try {
        const raw = fs.readFileSync(path.join(eventsDir, file), 'utf-8');
        const data = JSON.parse(raw);
        // Save the filename (without .json) so we can create a link to it!
        data.fileName = file.replace('.json', ''); 
        events.push(data);
    } catch (e) {
        console.error("Error parsing file:", file);
    }
});

// 3. Sort the events by Date (Newest first)
events.sort((a, b) => new Date(b.date) - new Date(a.date));

// 4. Save the master list
fs.writeFileSync(outputFile, JSON.stringify(events));
console.log(`Successfully built index for ${events.length} events!`);