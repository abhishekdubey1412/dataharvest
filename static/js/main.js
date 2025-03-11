document.addEventListener("DOMContentLoaded", function() {
    const toggleSwitch = document.getElementById("toggleSwitch");
    const urlForm = document.getElementById("urlForm");
    const fileForm = document.getElementById("fileForm");

    function addPaginationField(form) {
        let existingField = form.querySelector('input[name="pagination"]');
        if (existingField) {
            existingField.remove();
        }
        if (toggleSwitch.checked) {
            let hiddenInput = document.createElement("input");
            hiddenInput.type = "hidden";
            hiddenInput.name = "pagination";
            hiddenInput.value = "on";
            form.appendChild(hiddenInput);
        }
    }

    urlForm.addEventListener("submit", function() {
        addPaginationField(urlForm);
    });

    fileForm.addEventListener("submit", function() {
        addPaginationField(fileForm);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const rowsPerPage = 10;
    const table = document.getElementById("websites-table");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));
    const paginationContainer = document.createElement("div");
    paginationContainer.classList.add("pagination-container", "mt-3", "text-end");
    table.parentNode.appendChild(paginationContainer);

    let currentPage = 1;
    function displayPage(pageNumber) {
        const start = (pageNumber - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        rows.forEach((row, index) => {
            row.style.display = index >= start && index < end ? "" : "none";
        });
        currentPage = pageNumber;
        setupPagination();
    }

    function setupPagination() {
        paginationContainer.innerHTML = "";
        const totalPages = Math.ceil(rows.length / rowsPerPage);
        const maxVisiblePages = 5;
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, startPage + maxVisiblePages - 1);

        if (startPage > 1) {
            addPaginationButton("<", currentPage - 1);
            if (startPage > 2) {
                addPaginationButton("...", null);
            }
        }
        for (let i = startPage; i <= endPage; i++) {
            addPaginationButton(i, i);
        }
        if (endPage < totalPages) {
            if (endPage < totalPages - 1) {
                addPaginationButton("...", null);
            }
            addPaginationButton(">", currentPage + 1);
        }
    }

    function addPaginationButton(text, page) {
        const button = document.createElement("button");
        button.innerText = text;
        button.classList.add("btn", "btn-sm", "btn-outline-primary", "m-1");
        if (page === currentPage) {
            button.classList.add("active");
        }
        if (page !== null) {
            button.addEventListener("click", () => displayPage(page));
        } else {
            button.disabled = true;
        }
        paginationContainer.appendChild(button);
    }

    if (rows.length > rowsPerPage) {
        displayPage(1);
    }

    // Sorting functionality with button in headers
    document.querySelectorAll("#websites-table th").forEach((header, index) => {
        const sortButton = document.createElement("span");
        sortButton.innerHTML = " ↑";
        sortButton.dataset.order = "asc";
        header.appendChild(sortButton);

        header.style.cursor = "pointer";
        header.addEventListener("click", function () {
            const isAscending = sortButton.dataset.order === "asc";
            sortButton.dataset.order = isAscending ? "desc" : "asc";
            sortButton.innerHTML = isAscending ? " ↓" : " ↑";
            const sortedRows = rows.sort((rowA, rowB) => {
                const cellA = rowA.cells[index].textContent.trim();
                const cellB = rowB.cells[index].textContent.trim();
                return isAscending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
            });
            tbody.innerHTML = "";
            sortedRows.forEach(row => tbody.appendChild(row));
            displayPage(1);
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMDU2NjkxNTg1LCJpYXQiOjE3NDEzMzE1ODUsImp0aSI6IjhmMDdiZmJmZDZjMTQ1ZTY4MDZiMWQxYjVjZjU0Y2QxIiwidXNlcl9pZCI6MX0.7uoBSyMHE96ZkWTA-Y4U5yBnhjNw4vp7BQRuoWwg8A4";
    
    function fetchDataForWebsite(websiteId) {
      if (!websiteId) return;

      const apiUrl = `/api/domain-data/?url_id=${websiteId}`;
  
      fetch(apiUrl, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json"
            }
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          if (data[0]) {
            showDomainData([data[0]]);
          }
        })
        .catch(error => {
          console.error('Error fetching data:', error);
          hasError = true;
        });
    }
  
    function showDomainData(data) {
      const rowsContainer = document.getElementById('domainDataRows');
      const table = document.getElementById('domainDataTable');
      const heading = document.getElementById('domainDataHeading');
  
      if (!rowsContainer) {
        console.error('Error: Table body container not found');
        return;
      }
  
      rowsContainer.innerHTML = '';
      heading.style.display = 'block';
      table.style.display = 'block';
  
      data.forEach(domain => {
        const row = document.createElement('tr');
        const emails = Array.isArray(domain.emails) ? domain.emails.join(", ") : '';
        const phoneNumbers = Array.isArray(domain.phone_numbers) ? domain.phone_numbers.join(", ") : '';
        const socialMediaLinks = Array.isArray(domain.social_media_links) ? domain.social_media_links.join(", ") : '';
        const contactLinks = Array.isArray(domain.contact_links) ? domain.contact_links.join(", ") : '';
        const mxRecords = Array.isArray(domain.mx_records) ? domain.mx_records.join(", ") : '';
  
        row.innerHTML = `
          <td>${domain.domain || ''}</td>
          <td>${domain.title || ''}</td>
          <td>${emails}</td>
          <td>${phoneNumbers}</td>
          <td>${socialMediaLinks}</td>
          <td>${contactLinks}</td>
          <td>${mxRecords}</td>
          <td>${domain.mail_status || ''}</td>
          <td>${domain.mail_provider || ''}</td>
          <td>${domain.company_description || ''}</td>
          <td>${domain.created_at || ''}</td>
          <td>${domain.updated_at || ''}</td>
        `;
        rowsContainer.appendChild(row);
      });
    }

    function fetchScrapedData(id) {
        fetch(`/api/scraped-data/?url_id=${id}`, {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${accessToken}`,
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                const table = document.querySelector("#scrapedDataTable");
                const heading = document.querySelector("#scrapedDataHeading");
                heading.style.display = "block"
                const tableBody = table.querySelector("tbody");
    
                tableBody.innerHTML = "";
    
                if (data.error || data.length === 0) {
                    tableBody.innerHTML = `<tr><td colspan="5" class="text-center text-danger">No data available</td></tr>`;
                    table.style.display = "table";
                    return;
                }
    
                data.forEach(item => {
                    const socialLink = item.social_link 
                        ? `<a href="${item.social_link}" target="_blank">Profile</a>` 
                        : "N/A";
    
                    const row = `<tr>
                        <td>${item.name || "N/A"}</td>
                        <td>${item.email || "N/A"}</td>
                        <td>${item.phone || "N/A"}</td>
                        <td>${item.designation || "N/A"}</td>
                        <td>${socialLink}</td>
                    </tr>`;
                    tableBody.innerHTML += row;
                });
    
                table.style.display = "table"; // Ensure table is visible
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                const tableBody = document.querySelector("#scrapedDataTable tbody");
                tableBody.innerHTML = `<tr><td colspan="5" class="text-center text-danger">Error fetching data</td></tr>`;
                document.querySelector("#scrapedDataTable").style.display = "table";
            });
    }    

    function fetchRawTableData(id) {
        fetch(`/api/raw-data/?url_id=${id}`, {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${accessToken}`,
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (!Array.isArray(data)) {
                    console.error("Unexpected API response:", data);
                    return;
                }
    
                let tableHTML = "";
                let hasData = false;
    
                data.forEach((item, index) => {
                    if (typeof item.tables_data !== "object" || item.tables_data === null) {
                        console.warn("Missing or invalid tables_data for item:", item);
                        return;
                    }
    
                    Object.keys(item.tables_data).forEach(tableKey => {
                        const tableData = item.tables_data[tableKey];
    
                        if (!Array.isArray(tableData) || tableData.length === 0) {
                            return;
                        }
    
                        hasData = true;
                        const tableId = `data${index}-${tableKey.replace(/\s+/g, "-").toLowerCase()}`;
    
                        tableHTML += `
                            <div class="card shadow-lg rounded-3 border-0 mb-4" id="${tableId}">
                                <div class="card-header d-flex justify-content-between align-items-center bg-primary text-white">
                                    <h5 class="mb-0 text-uppercase fw-bold">${tableKey}</h5>
                                    <button type="button" class="btn btn-danger" onclick="window.DeleteTable('${tableId}', ${item.id})"> Delete Table </button>
                                </div>
                                <div class="card-body p-3">
                                    <div class="table-responsive" style="max-height: 400px; overflow-y: auto; overflow-x: auto;">
                                        <table class="table table-bordered table-striped table-hover align-middle">
                                            <thead class="table-dark text-center sticky-top">
                                                <tr id="header-${tableId}">`;
    
                        const columns = Object.keys(tableData[0]);
    
                        columns.forEach((col, index) => {
                            tableHTML += `<th id="col-${tableId}-${index}" class="p-2">
                                <div class="d-flex align-items-center justify-content-center">
                                    <select class="form-select form-select-sm w-auto me-2 shadow-sm" onchange="window.updateColumnName(this, '${tableId}', ${index})">
                                        <option value="${col}" selected>${col}</option>
                                        <option value="Name">Name</option>
                                        <option value="Email">Email</option>
                                        <option value="Phone">Phone</option>
                                        <option value="Designation">Designation</option>
                                        <option value="Social Link">Social Link</option>
                                    </select>
                                    <button class="btn btn-sm btn-danger px-2 py-1 delete-col-btn" id="delete-col-${tableId}-${index}" onclick="window.removeColumn('${tableId}', ${index})">❌</button>
                                </div>
                            </th>`;
                        });
    
                        tableHTML += `<th class="p-2">Actions</th>`;
                        tableHTML += `</tr></thead><tbody id="body-${tableId}">`;
    
                        tableData.forEach((row, rowIndex) => {
                            tableHTML += `<tr id="row-${tableId}-${rowIndex}">`;
                            columns.forEach((col) => {
                                tableHTML += `<td class="text-center">${row[col]}</td>`;
                            });
    
                            tableHTML += `<td class="text-center">
                                <button class="btn btn-sm btn-danger px-2 py-1" onclick="window.removeRow('${tableId}', ${rowIndex})">❌</button>
                            </td>`;
    
                            tableHTML += `</tr>`;
                        });
    
                        tableHTML += `</tbody></table></div>`;
    
                        // **Save & AI Cleaner Buttons**
                        tableHTML += `
                            <div class="d-flex justify-content-end mt-3">
                                <button class="btn btn-success me-2" onclick="window.showSavePopup('${tableId}', '${id}', '${item.id}')">💾 Save</button>
                                <button class="btn btn-warning" onclick="window.aiCleanTable('${tableId}')">🤖 AI Cleaner</button>
                            </div>`;
    
                        tableHTML += `</div></div>`;
                    });
                });
    
                if (hasData) {
                    document.getElementById("tablesWrapper").innerHTML = tableHTML;
                    document.getElementById("tableContainer").style.display = "block";
                } else {
                    document.getElementById("tableContainer").style.display = "none";
                    document.getElementById("tablesWrapper").innerHTML = "";
                }
            })
            .catch(error => console.error("Error fetching data:", error));
    }

    window.updateColumnName = function (selectElement, tableId, colIndex) {
        const newName = selectElement.value;
        selectElement.setAttribute("data-selected", newName);
    };
    
    window.DeleteTable = function (tableId, raw_id) {
        const tableElement = document.getElementById(tableId);
        const popupHTML = `
            <div id="deletePopup" class="position-fixed top-50 start-50 translate-middle p-4 shadow-lg rounded bg-white" style="width: 300px; z-index: 1050;">
                <h5 class="text-center">Confirm Deletion</h5>
                <p class="text-center text-muted">Are you sure you want to delete this table?</p>
                <div class="d-flex justify-content-between mt-3">
                    <button class="btn btn-secondary" onclick="window.closeDeletePopup()">Cancel</button>
                    <button class="btn btn-danger" onclick="window.confirmDeleteTable('${tableId}', '${raw_id}')">Delete</button>
                </div>
            </div>
            <div id="popupBackdrop" class="position-fixed top-0 start-0 w-100 h-100 bg-dark" style="z-index: 1049; opacity:0.5;"></div>
        `;
        document.body.insertAdjacentHTML("beforeend", popupHTML);
    };
    
    window.closeDeletePopup = function () {
        document.getElementById("deletePopup")?.remove();
        document.getElementById("popupBackdrop")?.remove();
    };
    
    window.confirmDeleteTable = function (tableId, raw_id) {

        fetch(`/api/raw-data/${raw_id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}`
            }
        })
        .then(response => response.json())
        .then(async data => {
            try {
                let tablesData = typeof data.tables_data === "string" ? JSON.parse(data.tables_data) : data.tables_data;
                const key = tableId.split("-")[1];
    
                if (key in tablesData) {
                    delete tablesData[key];
    
                    await fetch(`/api/raw-data/${raw_id}/`, {
                        method: "PATCH",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": `Bearer ${accessToken}`
                        },
                        body: JSON.stringify({ tables_data: tablesData })
                    })
                    .then(updateResponse => updateResponse.json())
                    .then(updatedData => {
                        console.log(`Key [${key}] removed and updated on server.`, updatedData);
                    })
                    .catch(updateError => console.error("Error updating data on server:", updateError));
                } else {
                    console.warn(`Key [${key}] not found in tablesData`);
                }
            } catch (error) {
                console.error("Error parsing tables_data:", error);
            }
        })
        .catch(error => console.error("Error fetching data:", error));

        const tableElement = document.getElementById(tableId);
        if (tableElement) {
            tableElement.remove();
        }
        window.closeDeletePopup();
    };
    
    window.removeColumn = function (tableId, colIndex) {
        const headerRow = document.querySelector(`#header-${tableId}`);
        const bodyRows = document.querySelectorAll(`#body-${tableId} tr`);
        
        console.log(tableId, colIndex, headerRow, bodyRows);
        
        if (headerRow && headerRow.children.length > colIndex) {
            headerRow.children[colIndex].remove();
        }
    
        bodyRows.forEach((row) => {
            if (row.children.length > colIndex) {
                row.children[colIndex].remove();
            }
        });
    };    
    
    window.removeRow = function (tableId, rowIndex) {
        const rowElement = document.getElementById(`row-${tableId}-${rowIndex}`);
        if (rowElement) {
            rowElement.remove();
        }
    };
    
    window.showSavePopup = function (tableId, id, raw_id) {
        const popupHTML = `
            <div id="savePopup" class="position-fixed top-50 start-50 translate-middle p-4 shadow-lg rounded bg-white" style="width: 300px; z-index: 1050;">
                <h5 class="text-center">Confirm Save</h5>
                <p class="text-center text-muted">Are you sure you want to save this table?</p>
                <div class="d-flex justify-content-between mt-3">
                    <button class="btn btn-secondary" onclick="window.closeSavePopup()">Cancel</button>
                    <button class="btn btn-primary" onclick="window.saveTable('${tableId}', ${id}, ${raw_id})">Save</button>
                </div>
            </div>
            <div id="popupBackdrop" class="position-fixed top-0 start-0 w-100 h-100 bg-dark" style="z-index: 1049; opacity:0.5;"></div>
        `;
        document.body.insertAdjacentHTML("beforeend", popupHTML);
    };
    
    window.closeSavePopup = function () {
        document.getElementById("savePopup")?.remove();
        document.getElementById("popupBackdrop")?.remove();
    };
    
    window.saveTable = async function (tableId, id, raw_id) {
        window.closeSavePopup();
        
        const table = document.querySelector(`#${tableId}`);
        if (!table) {
            console.error(`Table with ID ${tableId} not found!`);
            return;
        }
    
        let tableData = [];
    
        const headers = [];
        table.querySelectorAll("thead th").forEach(th => {
            const select = th.querySelector("select");
            headers.push(select ? select.value.trim() : th.textContent.trim());
        });
    
        table.querySelectorAll("tbody tr").forEach(row => {
            let rowData = {};
            row.querySelectorAll("td").forEach((cell, index) => {
                if (index < headers.length) {
                    rowData[headers[index]] = cell.innerText.trim();
                }
            });
            tableData.push(rowData);
        });
    
        console.log(`Table Data for ${tableId}:`, tableData);
    
        const saveRequests = tableData.map(row => {
            const requestData = {
                url_id: id,
                raw_id: raw_id,
                name: row.Name || "",
                email: row.Email || "",
                phone: row.Phone || "",
                designation: row.Designation || "",
                social_link: row["Social Link"] || ""
            };
    
            return fetch("/api/scraped-data/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${accessToken}`
                },
                body: JSON.stringify(requestData)
            })
            .then(response => response.json())
            .then(data => console.log("Saved Scraped Data:", data))
            .catch(error => console.error("Error saving data:", error));
        });
    
        await Promise.all(saveRequests);
    
        fetch(`/api/raw-data/${raw_id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}`
            }
        })
        .then(response => response.json())
        .then(async data => {
            try {
                let tablesData = typeof data.tables_data === "string" ? JSON.parse(data.tables_data) : data.tables_data;
                const key = tableId.split("-")[1];
    
                if (key in tablesData) {
                    delete tablesData[key];
    
                    await fetch(`/api/raw-data/${raw_id}/`, {
                        method: "PATCH",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": `Bearer ${accessToken}`
                        },
                        body: JSON.stringify({ tables_data: tablesData })
                    })
                    .then(updateResponse => updateResponse.json())
                    .then(updatedData => {
                        console.log(`Key [${key}] removed and updated on server.`, updatedData);
                    })
                    .catch(updateError => console.error("Error updating data on server:", updateError));
                } else {
                    console.warn(`Key [${key}] not found in tablesData`);
                }
            } catch (error) {
                console.error("Error parsing tables_data:", error);
            }
        })
        .catch(error => console.error("Error fetching data:", error));
    
        const tableContainer = document.getElementById(tableId);
        
        if (tableContainer) {
            tableContainer.remove();
            fetchScrapedData(id);
        }

    };  
    
    window.aiCleanTable = function (tableId) {
        const table = document.querySelector(`#${tableId} table`);
        if (!table) {
            console.error(`Table with ID ${tableId} not found!`);
            return;
        }
    
        let rawText = "";
    
        table.querySelectorAll("tbody tr").forEach(row => {
            let rowText = [];
            row.querySelectorAll("td").forEach(cell => {
                rowText.push(cell.innerText.trim());
            });
            rawText += rowText.join(" ") + "\n";
        });
    
        console.log("Extracted Raw Text:", rawText);
    
        const jsonPayload = { text: rawText };
    
        fetch('http://127.0.0.1:8000/staff-ai-extract/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonPayload)
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => { 
                    throw new Error(`Error: ${response.status}, ${text}`); 
                });
            }
            return response.json();
        })
        .then(responseData => {
            if (!responseData.data || !Array.isArray(responseData.data)) {
                console.error("Unexpected API Response Format:", responseData);
                return;
            }
            
            // Clear the existing table thead and tbody
            const thead = table.querySelector("thead");
            const tbody = table.querySelector("tbody");
            thead.innerHTML = "";
            tbody.innerHTML = "";

            // Create table headers dynamically if response contains data
            if (responseData.data.length > 0) {
                const theadRow = document.createElement("tr");
                Object.keys(responseData.data[0]).forEach(header => {
                    const th = document.createElement("th");
                    th.innerText = header.charAt(0).toUpperCase() + header.slice(1); // Capitalize headers
                    theadRow.appendChild(th);
                });
                thead.appendChild(theadRow);
            }

            // Populate table with API response data
            responseData.data.forEach(item => {
                const newRow = document.createElement("tr");
                Object.values(item).forEach(cellData => {
                    const newCell = document.createElement("td");
                    newCell.innerText = cellData || "-"; // If value is empty, show "-"
                    newRow.appendChild(newCell);
                });
                tbody.appendChild(newRow);
            });
        })
        .catch(error => {
            console.error("API Error:", error);
        });
    }; 
      
    window.showIdAndButton = function(id, button) {
      fetchDataForWebsite(id);
      fetchScrapedData(id);
      fetchRawTableData(id);
    };  
});