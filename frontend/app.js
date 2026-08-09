const API_BASE_URL = "http://127.0.0.1:8000";


// --------------------------------------------------
// Search query helper
// --------------------------------------------------

function setSearchQuery(query) {

    document.getElementById("searchInput").value = query;

}


// --------------------------------------------------
// Semantic Search
// --------------------------------------------------

async function searchDocuments() {

    const input =
        document.getElementById("searchInput");

    const button =
        document.getElementById("searchButton");

    const status =
        document.getElementById("searchStatus");

    const resultsContainer =
        document.getElementById("searchResults");


    const query = input.value.trim();


    if (!query) {

        status.innerText =
            "Please enter a search query.";

        return;
    }


    button.disabled = true;

    button.innerText = "Searching...";

    status.innerText =
        "Searching investor documents...";

    resultsContainer.innerHTML = "";


    try {

        const response = await fetch(
            `${API_BASE_URL}/search`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    query: query,
                    n_results: 5
                })
            }
        );


        if (!response.ok) {

            throw new Error(
                `Search failed (${response.status})`
            );

        }


        const data =
            await response.json();


        status.innerText =
            `Found ${data.results.length} relevant results.`;


        if (data.results.length === 0) {

            resultsContainer.innerHTML =
                `<div class="result">
                    No relevant documents found.
                </div>`;

            return;
        }


        data.results.forEach(
            (result, index) => {

                const div =
                    document.createElement("div");


                div.className = "result";


                const metadata =
                    result.metadata || {};


                const distance =
                    typeof result.distance === "number"
                        ? result.distance.toFixed(4)
                        : "N/A";


                div.innerHTML = `

                    <div class="result-header">

                        <span class="result-number">
                            Result ${index + 1}
                        </span>

                        <span class="distance">
                            Distance: ${distance}
                        </span>

                    </div>


                    <div class="result-document">
                        ${escapeHtml(result.document)}
                    </div>


                    <div class="metadata">

                        <strong>Company:</strong>
                        ${escapeHtml(
                            metadata.company || "N/A"
                        )}

                        <br>

                        <strong>Document:</strong>
                        ${escapeHtml(
                            metadata.filename || "N/A"
                        )}

                        <br>

                        <strong>Chunk:</strong>
                        ${escapeHtml(
                            String(
                                metadata.chunk_index ??
                                metadata.chunk ??
                                "N/A"
                            )
                        )}

                    </div>

                `;


                resultsContainer.appendChild(div);

            }
        );


    } catch (error) {

        console.error(error);

        status.innerText =
            "Could not connect to the backend. "
            + "Make sure FastAPI is running.";

    } finally {

        button.disabled = false;

        button.innerText = "Search";

    }

}


// --------------------------------------------------
// AI Summary
// --------------------------------------------------

async function generateSummary() {

    const input =
        document.getElementById("summaryInput");

    const button =
        document.getElementById("summaryButton");

    const status =
        document.getElementById("summaryStatus");

    const resultContainer =
        document.getElementById("summaryResult");


    const text =
        input.value.trim();


    if (!text) {

        status.innerText =
            "Please enter document text.";

        return;
    }


    button.disabled = true;

    button.innerText =
        "Generating...";


    status.innerText =
        "Gemini is analyzing the document...";


    resultContainer.innerText = "";


    try {

        const response = await fetch(
            `${API_BASE_URL}/summarize`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: text
                })
            }
        );


        if (!response.ok) {

            throw new Error(
                `Summary failed (${response.status})`
            );

        }


        const data =
            await response.json();


        status.innerText =
            "AI summary generated successfully.";


        resultContainer.innerHTML =DOMPurify.sanitize(marked.parse(data.summary));


    } catch (error) {

        console.error(error);

        status.innerText =
            "Could not generate the summary. "
            + "Make sure the backend is running.";

    } finally {

        button.disabled = false;

        button.innerText =
            "Generate AI Summary";

    }

}


// --------------------------------------------------
// Clear summary
// --------------------------------------------------

function clearSummary() {

    document.getElementById(
        "summaryInput"
    ).value = "";

    document.getElementById(
        "summaryResult"
    ).innerText = "";

    document.getElementById(
        "summaryStatus"
    ).innerText = "";

}


// --------------------------------------------------
// Basic HTML escaping
// --------------------------------------------------

function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}