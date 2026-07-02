let page =1;
let currentBranch= "";
let currentSemester= "";
let currentYear= "";

function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1] || '';
}

//  HTML for a single paper card
function createPaperCard(paper) {
    const isBookmarked = paper.is_bookmarked || false;
    const heartColor = isBookmarked ? 'red' : 'black';
    const heartIcon = isBookmarked ? '❤️' : '🤍';
    
    return `
        <div class="paper-card">
            <h3>${paper.title}</h3>
            <p>${paper.code}</p>
            <p>${paper.branch}</p>
            <p>Semester: ${paper.semester}</p>
            <p>${paper.year}</p>
            <a href="/api/subjects/${paper.subject_id}">
                View Papers
            </a>
            <button class="toggle_bookmark" data-paper-id="${paper.id}">
                <span class="bookmark-icon" style="color: ${heartColor};">${heartIcon}</span>
                <span class="bookmark_message"></span>
            </button>
        </div>
    `;
}

// Handle bookmark button click
function handleBookmarkClick(btn) {
    const paperId = btn.dataset.paperId;
    const icon = btn.querySelector('.bookmark-icon');
    const msg = btn.querySelector('.bookmark_message');
    
    fetch(`/api/bookmark/${paperId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.bookmarked) {
            icon.textContent = '❤️';
            icon.style.color = 'red';
            msg.textContent = 'Bookmarked!';
        } else {
            icon.textContent = '🤍';
            icon.style.color = 'black';
            msg.textContent = 'Removed';
        }
        setTimeout(() => msg.textContent = '', 3000);
    })
    .catch(error => console.error('Bookmark error:', error));
}

// click listeners to all bookmark buttons
function attachBookmarkListeners() {
    document.querySelectorAll(".toggle_bookmark").forEach(btn => {
        btn.onclick = function() {
            handleBookmarkClick(this);
        };
    });
}


// search

const searchBox = document.getElementById("search-box");
const results = document.getElementById("results");

if (searchBox) {
    searchBox.addEventListener("input", async function() {
        let query = searchBox.value;
        if (query.length < 2) {
            results.innerHTML = "";
            return;
        }
        
        try {
            const response = await fetch(`api/search/?q=${query}`);
            const data = await response.json();
            results.innerHTML = "";
            data.forEach(subject => {
                results.innerHTML += `
                    <div>
                        <a href="api/subjects/${subject.id}/">
                            ${subject.title}
                            <small>${subject.code}</small>
                        </a>
                    </div>
                `;
            });
        } catch(error) {
            console.error("search_error:", error);
        }
    });
}



async function displayPapers(url) {
    const paperContainer = document.getElementById("paper-container");
    if (!paperContainer) return;
    
    try {
        const response = await fetch(url);
        const data = await response.json();
        const papers = data.papers || data; // Handle both paginated and non-paginated responses
        
        paperContainer.innerHTML = "";
        
        if (!papers || papers.length === 0) {
            paperContainer.innerHTML = "<p>No papers found.</p>";
            return;
        }
        
        papers.forEach(paper => {
            paperContainer.innerHTML += createPaperCard(paper);
        });
        
        attachBookmarkListeners();
        const pageInfo = document.getElementById("page-info");
        const prevBtn = document.getElementById("prev-btn");
        const nextBtn = document.getElementById("next-btn");

        if (pageInfo && prevBtn && nextBtn && data.current_page){
            pageInfo.textContent = `page ${data.current_page} of ${data.total_pages}`;

            prevBtn.disabled = !data.has_previous;
            nextBtn.disabled = !data.has_next;

        }
        
    } catch(error) {
        console.error('Error loading papers:', error);
        paperContainer.innerHTML = "<p>Error loading papers. Please try again.</p>";
    }
}



const applyBtn = document.getElementById("apply-btn");

if (applyBtn) {
    applyBtn.addEventListener("click", function() {
        currentBranch = document.querySelector('[name="branch"]').value;
        currentSemester = document.querySelector('[name="semester"]').value;
        currentYear = document.querySelector('[name="year"]').value;
        page =1;
        
        const url = `/api/papers/?page=${page}&branch=${currentBranch}&semester=${currentSemester}&year=${currentYear}`;
        displayPapers(url);
    });
}

const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");
console.log(nextBtn)
if (prevBtn){
    prevBtn.onclick = function(){
        if (page > 1){
            page --;
            const url = `/api/papers/?page=${page}&branch=${currentBranch}&semester=${currentSemester}&year=${currentYear}`;
            displayPapers(url);
        }
    };
}

if (nextBtn){
    nextBtn.onclick = function(){
        page++;
        const url = `/api/papers/?page=${page}&branch=${currentBranch}&semester=${currentSemester}&year=${currentYear}`;
        console.log(url)
        displayPapers(url);

    };
}



if (document.getElementById("paper-container")) {
    displayPapers('/api/papers/');
}



const input = document.getElementById("profileInput");
const preview = document.getElementById("profilePreview");

if (input && preview) {
    input.addEventListener("change", function() {
        const file = this.files[0];
        if (file) {
            preview.src = URL.createObjectURL(file);
        }
    });
}