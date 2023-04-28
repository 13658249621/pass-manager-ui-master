
function copyToClipboard(text, callback){
  let transfer = document.createElement('input');
  document.body.appendChild(transfer);
  transfer.value = text;  // 这里表示想要复制的内容
  transfer.focus();
  transfer.select();
  if (document.execCommand('copy')) {
    document.execCommand('copy');
  }
  transfer.blur();
  document.body.removeChild(transfer);
  if (callback!==undefined){
    callback()
  }
}
export default copyToClipboard
