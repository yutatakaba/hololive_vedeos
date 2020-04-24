const API_URL_PREFIX = 'http://127.0.0.1:5000';
const urlParams = new URLSearchParams(window.location.search);
const day = urlParams.get("day");

new Vue({
  el: '#main',
  data() {
    return {
      videoInfos: []    // 動画情報
    }
   },

  created() {
    console.log('hoge');
    // 動画情報取得
    axios
      .get(API_URL_PREFIX + '/site_api/v1/day_data/' + day)
      .then(response => {
        this.videoInfos = this.videoInfos.concat(response.data.day_video_datas);

        console.log(this.videoInfos);
        console.log(response);
      })
      .catch(error => {
        console.log(error)
      });
    console.log(this.videoInfos);
  }
});
