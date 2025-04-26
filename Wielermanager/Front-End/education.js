const jobs = [
    "Applicatie- en databeheer", "Context 4 Omgeving en duurzame ontwikkeling", "Gezondheidszorg",
    "Optiektechnieken", "Binnenvaarttechnieken", "Defensie en veiligheid", "Muziek", "Opvoeding en begeleiding",
    "Sportwetenschappen", "Wetenschappen-Wiskunde", "Grieks-Wiskunde", "Ballet", "Project Algemene Vakken",
    "Natuurwetenschappen", "Horeca", "Freinetpedagogie", "Architectuur en interieur",
    "Biotechnologische en chemische technieken", "Informatica- en communicatiewetenschappen",
    "Taal en communicatie", "Lichamelijke Opvoeding", "Grieks/Latijn", "Moderne Vreemde Talen Frans - Engels",
    "Bakkerijtechnieken", "Rudolf Steinerpedagogie", "Beeldende vorming", "Dans", "Sport",
    "Economie-Wiskunde", "Dentaaltechnieken", "Maritieme technieken motoren", "Latijn-Moderne talen",
    "Textielontwerp en prototyping", "Bouw- en houtwetenschappen", "Yeshiva", "Crossmedia",
    "Slagerij-Traiteurtechnieken", "Topsport (dubbele finaliteit)", "Beeldende kunst", "Autotechnieken",
    "Taal en communicatiewetenschappen", "Technologische wetenschappen en engineering",
    "Textielproductietechnieken", "Wellness en schoonheid", "Welzijnswetenschappen",
    "Bedrijfsondersteunende Informaticawetenschappen", "Moderne Vreemde Talen Duits",
    "Agrotechnieken dier", "Internationale handel en logistiek",
    "Biotechnologische en chemische wetenschappen", "Mechanische vormgevingstechnieken",
    "Industriële ICT", "Context 2 Mentale gezondheid", "Context 5 Politiek-juridische samenleving",
    "Elektromechanische technieken", "Elektronicatechnieken", "Woordkunst-drama", "Podiumtechnieken",
    "Fotografie", "Commerciële organisatie", "Leren Leren", "Aardrijkskunde", "Technisch-Technologische Vorming",
    "Mechatronica", "Humane Wetenschappen", "Humane wetenschappen", "Geschiedenis", "Grafimedia",
    "Dierenverzorgingstechnieken", "Moderne talen-Wetenschappen", "Context 7 Socio culturele samenleving",
    "Moderne talen (derde graad)", "Sportbegeleiding", "Tuinaanleg en beheer", "Topsport-Wetenschappen",
    "Moderne Talen", "Economie", "Koel- en warmtetechnieken", "Bedrijfswetenschappen",
    "Architecturale vorming", "Topsport-Bedrijfswetenschappen", "Wiskunde", "Elektrotechnieken",
    "Natuur- en groentechnieken", "Toerisme", "Maritieme technieken dek", "Grieks-Latijn",
    "Orthopedietechnieken", "Audiovisuele vorming", "Stam", "Topsport", "Mode",
    "Context 3 Sociorelationele ontwikkeling", "Latijn-Wiskunde", "Context 1 Lichamelijke gezondheid en veiligheid",
    "Nederlands", "Bedrijfsorganisatie", "Agrotechnieken plant", "Wetenschappen",
    "Economie-Moderne talen", "Bouwtechnieken", "Latijn-Wetenschappen",
    "Biotechnologische en chemische STEM-wetenschappen", "Topsport-Economie",
    "Context 6 Socio-economische samenleving", "Moderne vreemde talen Frans of Engels", "Houttechnieken",
    "Vliegtuigtechnieken"
];

document.addEventListener('DOMContentLoaded', function() {
    const jobSearchContainer = document.querySelector('.job-search-container');
    const jobListEl = document.getElementById("jobList");
    const inputEl = document.getElementById("jobSearchInput");
    const yearInputEl = document.getElementById("yearInput");

    // Replace the select dropdown with a div for better visualization
    jobListEl.style.display = 'none'; // Hide the original select element
    
    // Create a visible options container
    const visibleOptionsContainer = document.createElement('div');
    visibleOptionsContainer.id = 'visibleOptions';
    visibleOptionsContainer.className = 'visible-options';
    visibleOptionsContainer.style.display = 'none'; // Initially hidden
    jobSearchContainer.querySelector('.input-group').appendChild(visibleOptionsContainer);
    
    // Add CSS for the visible options container
    const style = document.createElement('style');
    style.textContent = `
        .visible-options {
            max-height: 300px;
            overflow-y: auto;
            border: 1px solid #ccc;
            border-top: none;
            background-color: white;
            width: 100%;
            position: absolute;
            z-index: 1000;
            margin-top: -1px;
        }
        .option-item {
            padding: 8px 12px;
            cursor: pointer;
        }
        .option-item:hover {
            background-color: #f0f0f0;
        }
        .input-group {
            position: relative;
        }
    `;
    document.head.appendChild(style);

    function displayOptions(filter = "") {
        const filtered = jobs
            .filter(job => job.toLowerCase().includes(filter.toLowerCase()))
            .sort();
        
        visibleOptionsContainer.innerHTML = "";
        
        filtered.forEach(job => {
            const optionItem = document.createElement('div');
            optionItem.className = 'option-item';
            optionItem.textContent = job;
            optionItem.addEventListener('click', () => {
                inputEl.value = job;
                visibleOptionsContainer.style.display = 'none';
                
                // Also update the hidden select for form submission
                const option = document.createElement('option');
                option.value = job;
                option.selected = true;
                jobListEl.innerHTML = '';
                jobListEl.appendChild(option);
            });
            visibleOptionsContainer.appendChild(optionItem);
        });
    }

    // Show options when clicking on the input
    inputEl.addEventListener('click', () => {
        displayOptions(inputEl.value);
        visibleOptionsContainer.style.display = 'block';
    });

    // Filter options when typing
    inputEl.addEventListener('input', () => {
        displayOptions(inputEl.value);
        visibleOptionsContainer.style.display = 'block';
    });

    // Hide options when clicking outside
    document.addEventListener('click', (event) => {
        if (!jobSearchContainer.contains(event.target)) {
            visibleOptionsContainer.style.display = 'none';
        }
    });

    yearInputEl.addEventListener("input", () => {
        console.log("Ingegeven jaar:", yearInputEl.value);
        // Hier kan je later nog iets doen met de jaarinput, zoals filteren per jaartal
    });

    // Initial setup - prepare the options
    displayOptions();

    document.getElementById('zoekForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Zorgt ervoor dat de pagina niet herlaadt
        alert('Formulier is verzonden!');
    });
});