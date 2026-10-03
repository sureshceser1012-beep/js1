function saveTheme(theme) {
    localStorage.setItem("appTheme", theme);
}

function loadTheme() {
    return localStorage.getItem("appTheme");
}

function storeSessionToken(token) {
    sessionStorage.setItem("sessionToken", token);
}

function clearSessionToken() {
    sessionStorage.removeItem("sessionToken");
}