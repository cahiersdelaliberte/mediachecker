
function highlightRange(range) {
    var newNode = document.createElement("span");
    newNode.setAttribute(
        "style",
        "background-color: yellow;"
    );
    range.surroundContents(newNode);
}

function highlightRangeOfElement(rangeId) {
    var range = document.createRange();
    range.selectNode(document.getElementById(rangeId))
    highlightRange(range)
}

function highlightSelection() {
    var userSelection = window.getSelection();
    for(var i = 0; i < userSelection.rangeCount; i++) {
        highlightRange(userSelection.getRangeAt(i));
    } 
}

function highlightTextInElement(id, what) {
    var container = document.getElementById(id),
        replaceWith = '$1<mark>$2</mark>$3'
        //Or: replaceWith = '$1<span class="highlight">$2</span>$3'
    return replaceExpression(container, what, replaceWith)
}

function replaceExpression(container, what, replaceWith) {
    var content = container.innerHTML,
        pattern = new RegExp('(>[^<.]*)(' + what + ')([^<.]*)','g'),
        highlighted = content.replace(pattern, replaceWith);
    // This will return false if the word was not found.
    return (container.innerHTML = highlighted) !== content;
}

/**
 * Highlight keywords inside a DOM element
 * @param {string} elem Element to search for keywords in
 * @param {string[]} keywords Keywords to highlight
 * @param {boolean} caseSensitive Differenciate between capital and lowercase letters
 * @param {string} cls Class to apply to the highlighted keyword
 * src: https://stackoverflow.com/questions/8644428/how-to-highlight-text-using-javascript
 */
//Example: Highlight all keywords found in the page (needs css class 'highlight')
//highlight(document.body, ['lorem', 'amet', 'autem']);
function highlight(elem, keywords, caseSensitive = false, cls = 'highlight') {
    const flags = caseSensitive ? 'gi' : 'g';
    // Sort longer matches first to avoid
    // highlighting keywords within keywords.
    keywords.sort((a, b) => b.length - a.length);
    Array.from(elem.childNodes).forEach(child => {
      const keywordRegex = RegExp(keywords.join('|'), flags);
      if (child.nodeType !== 3) { // not a text node
        highlight(child, keywords, caseSensitive, cls);

      } else if (keywordRegex.test(child.textContent)) {
        const frag = document.createDocumentFragment();
        let lastIdx = 0;
        child.textContent.replace(keywordRegex, (match, idx) => {
          const part = document.createTextNode(child.textContent.slice(lastIdx, idx));
          const highlighted = document.createElement('span');
          highlighted.textContent = match;
          highlighted.classList.add(cls);
          frag.appendChild(part);
          frag.appendChild(highlighted);
          lastIdx = idx + match.length;
        });
        const end = document.createTextNode(child.textContent.slice(lastIdx));
        frag.appendChild(end);
        child.parentNode.replaceChild(frag, child);
      }
    });
}
