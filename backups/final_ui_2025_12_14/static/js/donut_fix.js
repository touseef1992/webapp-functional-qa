/* donut_fix.js - robust removal + overlay */
(function(){
  function removeSmallText(root){
    if(!root) return;
    // remove svg text and short nodes
    try {
      root.querySelectorAll('svg text, svg tspan').forEach(function(n){
        var t=(n.textContent||'').trim();
        if(t.length && t.length < 8) n.remove();
        else { n.style.display='none'; n.style.visibility='hidden'; }
      });
    } catch(e){}
    // remove stray small div/span/p
    try {
      Array.from(root.querySelectorAll('div, span, p')).forEach(function(n){
        var t=(n.textContent||'').trim();
        if(!t) return;
        if(t.length < 8 || /ions$/i.test(t)) n.remove();
      });
    } catch(e){}
  }

  function addOverlay(root){
    var donut = root.querySelector('canvas, svg');
    if(!donut) return;
    var parent = donut.parentElement || root;
    parent.classList.add('donut-wrapper');
    var overlay = parent.querySelector('.donut-center-overlay');
    if(!overlay){
      overlay = document.createElement('div');
      overlay.className='donut-center-overlay';
      overlay.innerHTML = '<div class=\"label\">Sessions</div><div class=\"value\">—</div>';
      parent.appendChild(overlay);
    }
    // attempt to set value from legend
    try {
      var m = (root.innerText||'').match(/\\b(\\d{1,6})\\b/);
      if(m) overlay.querySelector('.value').textContent = m[1];
    } catch(e){}
    // size overlay
    try {
      var r=donut.getBoundingClientRect();
      var dim=Math.min(r.width,r.height);
      var size=Math.max(60,Math.floor(dim*0.42));
      overlay.style.width = size+'px';
      overlay.style.height = size+'px';
      overlay.style.borderRadius = Math.ceil(size/2) + 'px';
    } catch(e){}
  }

  function runAll(){
    // try to find donut container heuristically
    var root = document.querySelector('.user-sessions-map') || document.querySelector('[aria-label*=\"User Sessions\"]') || document.querySelector('.sessions') || document.querySelector('.chart') || document.body;
    if(!root) { return; }
    removeSmallText(root);
    addOverlay(root);
    // schedule retries
    setTimeout(function(){ removeSmallText(root); addOverlay(root); }, 200);
    setTimeout(function(){ removeSmallText(root); addOverlay(root); }, 800);
  }

  document.addEventListener('DOMContentLoaded', runAll);
  window.addEventListener('load', runAll);
  window.addEventListener('resize', function(){ setTimeout(runAll,150); });
  window.__donutFixRun = runAll;
})();
