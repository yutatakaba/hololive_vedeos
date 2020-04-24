const API_URL_PREFIX = 'http://127.0.0.1:5000';
const date = new Date();
let year = date.getFullYear();
let month = date.getMonth() + 1;

new Vue({
  el: '#main',
  data() {
    return {
      dayVideoInfos: []   // 動画情報
    }
  },

  created() {
    // 動画情報取得
    console.log('hoge');
    axios
      .get(API_URL_PREFIX + '/site_api/v1/month_data?year=' + year + '&month=' + month)
      .then(response => {
        this.dayVideoInfos = this.dayVideoInfos.concat(response.data.month_video_data);
        console.log(this.dayVideoInfos);
        console.log(response);
      })
      .catch(error => {
        console.log(error)
      });
    console.log(this.dayVideoInfos);
  }
});
