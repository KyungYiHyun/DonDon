<template>
  <div class="container">
    <!-- <h3 class="border-bottom py-2">은행 검색</h3> -->
    <div class="title-section text-center">
      <h2 class="main-title animate-typing">주변 은행 찾기</h2>
      <p class="sub-title animate-fade">언제 어디서든 내 주변에 있는 가장 가까운 은행을 찾아보세요!</p>
    </div>
    <div class="row">
      <!-- 왼쪽: 지역/은행 선택 -->
      <div class="col-md-3 col-sm-12 p-3">
        <form @submit.prevent="searchBank">
          <!-- 행정구역 선택 -->
          <div class="mb-3">
            <label for="province" class="form-label">특별시/광역시/도</label>
            <select
              id="province"
              v-model="province"
              @change="updateRegion"
              class="form-control"
            >
              <option disabled value="">선택</option>
              <option v-for="province in provinces" :key="province">
                {{ province }}
              </option>
            </select>
          </div>
          <div class="mb-3">
            <label for="city" class="form-label">시/군/구</label>
            <select
              id="city"
              v-model="city"
              @change="updateRegion"
              :disabled="!province"
              class="form-control"
            >
              <option disabled value="">선택</option>
              <option v-for="city in cities[province]" :key="city">
                {{ city }}
              </option>
            </select>
          </div>
          <!-- 은행 선택 -->
          <div class="mb-3">
            <label for="bankName" class="form-label">은행</label>
            <select id="bankName" v-model="bankName" class="form-control">
              <option disabled value="">선택</option>
              <option v-for="bank in banks" :key="bank">{{ bank }}</option>
            </select>
          </div>
          <button class="btn-custom w-100 mb-4">
            <i class="fa-solid fa-map-location-dot p-1"></i>
            검색
          </button>
        </form>
        <!-- <span style="font-size: 14px; font-weight: 600;" >은행만 선택하면 현재 위치에서 가장 가까운 은행을 검색합니다!</span> -->
      </div>

      <!-- 오른쪽: 지도 -->
      <div class="col-md-9 col-sm-12 p-3">
        <div id="map"></div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
const provinces = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원특별자치도','충청북도', '충청남도', '전라북도', '전라남도','경상북도','경상남도','제주특별자치도']
const cities = {
  "서울특별시": ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"],
  "부산광역시": ["강서구", "금정구", "기장군", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구"],
  "대구광역시": ["남구", "달서구", "달성군", "동구", "북구", "서구", "수성구", "중구", "군위군"],
  "인천광역시": ["강화군", "계양구", "남동구", "동구", "미추홀구", "부평구", "서구", "연수구", "옹진군", "중구"],
  "광주광역시": ["광산구", "남구", "동구", "북구", "서구"],
  "대전광역시": ["대덕구", "동구", "서구", "유성구", "중구"],
  "울산광역시": ["남구", "동구", "북구", "울주군", "중구"],
  "세종특별자치시": ["세종특별자치시"],
  "경기도": ["가평군", "고양시", "과천시", "광명시", "광주시", "구리시", "군포시", "김포시", "남양주시", "동두천시", "부천시", "성남시", "수원시", "시흥시", "안산시", "안성시", "안양시", "양주시", "양평군", "여주시", "연천군", "오산시", "용인시", "의왕시", "의정부시", "이천시", "파주시", "평택시", "포천시", "하남시", "화성시"],
  "강원특별자치도": ["강릉시", "고성군", "동해시", "삼척시", "속초시", "양구군", "양양군", "영월군", "원주시", "인제군", "정선군", "철원군", "춘천시", "태백시", "평창군", "홍천군", "화천군", "횡성군"],
  "충청북도": ["괴산군", "단양군", "보은군", "영동군", "옥천군", "음성군", "제천시", "증평군", "진천군", "청주시", "충주시"],
  "충청남도": ["계룡시", "공주시", "금산군", "논산시", "당진시", "보령시", "부여군", "서산시", "서천군", "아산시", "예산군", "천안시", "청양군", "태안군", "홍성군"],
  "전라북도": ["고창군", "군산시", "김제시", "남원시", "무주군", "부안군", "순창군", "완주군", "익산시", "임실군", "장수군", "전주시", "정읍시", "진안군"],
  "전라남도": ["강진군", "고흥군", "곡성군", "광양시", "구례군", "나주시", "담양군", "목포시", "무안군", "보성군", "순천시", "신안군", "여수시", "영광군", "영암군", "완도군", "장성군", "장흥군", "진도군", "함평군", "해남군", "화순군"],
  "경상북도": ["경산시", "경주시", "고령군", "구미시", "김천시", "문경시", "봉화군", "상주시", "성주군", "안동시", "영덕군", "영양군", "영주시", "영천시", "예천군", "울릉군", "울진군", "의성군", "청도군", "청송군", "칠곡군", "포항시"],
  "경상남도": ["거제시", "거창군", "고성군", "김해시", "남해군", "밀양시", "사천시", "산청군", "양산시", "의령군", "진주시", "창녕군", "창원시", "통영시", "하동군", "함안군", "함양군", "합천군"],
  "제주특별자치도": ["서귀포시", "제주시"]
}
const banks = ['KB국민은행','신한은행', '하나은행', '우리은행', 'NH농협은행', 'IBK기업은행', 'SC제일은행', '한국씨티은행', 'IM뱅크', 'BNK부산은행', '광주은행', '제주은행', '전북은행', 'BNK경남은행', '케이뱅크', '카카오뱅크', '토스뱅크']
const provinceMapping = {
  '서울특별시': '서울',
  '부산광역시': '부산',
  '대구광역시': '대구',
  '인천광역시': '인천',
  '광주광역시': '광주',
  '대전광역시': '대전',
  '울산광역시': '울산',
  '세종특별자치시': '세종',
  '경기도': '경기',
  '강원특별자치도': '강원',
  '충청북도': '충북',
  '충청남도': '충남',
  '전라북도': '전북',
  '전라남도': '전남',
  '경상북도': '경북',
  '경상남도': '경남',
  '제주특별자치도': '제주'
}

const map = ref(null) // 지도 객체
const markerImage = ref(null) // 커스텀 마커
const markers = ref([])
const province = ref('') // 도/특별시/광역시
const city = ref('') // 시/군/구
const region = ref('') // 선택된 행정구역
const bankName = ref('') // 은행명
const searchProvince = ref('') // 축약된 도/특별시/광역시

const activeInfoWindow = ref(null) // 현재 열려 있는 인포 윈도우


// 행정구역 업데이트
const updateRegion = () => {

  if (province.value) {
    // 축약된 이름으로 저장
    searchProvince.value = provinceMapping[province.value] || province.value
  } 
  if (province.value && city.value) {
    region.value = `${searchProvince.value} ${city.value}`
  }
}
const nowLat = ref('')
const nowLng = ref('')

const latlng = ref({})
console.log(latlng)

const options = {
  enableHighAccuracy: true
}
// 초기 지도 로드
onMounted(() => {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const lat = position.coords.latitude
      const lng = position.coords.longitude
      nowLat.value = lat
      nowLng.value = lng
      
      // 지도를 현재 위치로 초기화
      const mapContainer = document.getElementById('map')
      const mapOption = {
        center: new kakao.maps.LatLng(lat, lng),
        level: 4,
      }
      map.value = new kakao.maps.Map(mapContainer, mapOption)

      // 현재 위치 마커 추가
      const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png' // 커스텀 이미지
      const imageSize = new kakao.maps.Size(24, 35)
      markerImage.value = new kakao.maps.MarkerImage(imageSrc, imageSize)

      new kakao.maps.Marker({
        map: map.value,
        position: new kakao.maps.LatLng(lat, lng),
        image: markerImage.value,
      })
    },
    (error) => {
      console.error('현재 위치를 가져올 수 없습니다:', error)
    },
    options
  )
})

//마커 삭제
const clearMarkers = () => {
  markers.value.forEach((marker) => marker.setMap(null)) // 기존 마커 삭제
  markers.value = [] // 배열 초기화
  if (activeInfoWindow.value) {
    activeInfoWindow.value.close() // 열려 있는 인포 윈도우 닫기
    activeInfoWindow.value = null // 초기화
  }
}
const searchBank = () => {
  if (!region.value && !bankName.value.trim()) {
    alert("원하는 지역과 은행명을 입력해주세요.")
    return
  }

  clearMarkers() // 기존 마커 삭제

  if (!region.value && bankName.value.trim()) {
    const ps = new kakao.maps.services.Places()
    const currentLocation = new kakao.maps.LatLng(nowLat.value, nowLng.value)

    ps.keywordSearch(`${bankName.value}`, (data, status) => {
      if (status === kakao.maps.services.Status.OK) {
        const bounds = new kakao.maps.LatLngBounds()

        // 검색 결과에서 ATM을 제외하고 현재 위치 근처만 필터링
        const filteredData = data.filter((place) => {
          return !place.category_name.includes("ATM")
        })

        if (filteredData.length === 0) {
          alert("현재 위치 근처에 해당 은행이 없습니다.")
          return
        }

        filteredData.forEach((place) => {
          const marker = new kakao.maps.Marker({
            map: map.value,
            position: new kakao.maps.LatLng(place.y, place.x),
          })

          const infowindow = new kakao.maps.InfoWindow({
            content: `<div style="overflow: hidden; padding:5px; font-size: 14px; white-space: nowrap; text-align: center;">${place.place_name}</div>`,
          })

          kakao.maps.event.addListener(marker, "click", () => {
            if (activeInfoWindow.value) {
              activeInfoWindow.value.close()
            }
            infowindow.open(map.value, marker)
            activeInfoWindow.value = infowindow
          })

          markers.value.push(marker)
          bounds.extend(new kakao.maps.LatLng(place.y, place.x))
        })

        map.value.setBounds(bounds) // 지도 범위를 검색 결과에 맞게 조정
      } else {
        alert("검색 결과가 없습니다.")
      }
    }, {
      location: currentLocation, // 현재 위치 기준으로 검색
      radius: 3000, // 반경 3km
    })
    return
  }
  const geocoder = new kakao.maps.services.Geocoder()
  geocoder.addressSearch(region.value, (result, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const coords = new kakao.maps.LatLng(result[0].y, result[0].x)
      map.value.setCenter(coords) // 지도 중심 이동

      const ps = new kakao.maps.services.Places()
      ps.keywordSearch(`${region.value} ${bankName.value}`, (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
          const bounds = new kakao.maps.LatLngBounds()

          const filteredData = data.filter((place) => {
            const address = place.address_name || place.road_address_name
            return (
              address.includes(searchProvince.value) &&
              address.includes(city.value) &&
              !place.category_name.includes("ATM")
            )
          })

          if (filteredData.length === 0) {
            alert("선택한 지역에 해당하는 검색 결과가 없습니다.")
            return
          }

          filteredData.forEach((place) => {
            const marker = new kakao.maps.Marker({
              map: map.value,
              position: new kakao.maps.LatLng(place.y, place.x),
            })

            const infowindow = new kakao.maps.InfoWindow({
              content: `<div style="overflow: hidden; padding:5px; font-size: 14px; white-space: nowrap; text-align: center;">${place.place_name}</div>`,
            })

            kakao.maps.event.addListener(marker, "click", () => {
              if (activeInfoWindow.value) {
                activeInfoWindow.value.close()
              }
              infowindow.open(map.value, marker)
              activeInfoWindow.value = infowindow
            })

            markers.value.push(marker)
            bounds.extend(new kakao.maps.LatLng(place.y, place.x))
          })

          map.value.setBounds(bounds)
        } else {
          alert("검색 결과가 없습니다.")
        }
      })
    } else {
      alert("선택한 지역을 찾을 수 없습니다.")
    }
  })
}
</script>

<style scoped>
#map {
  width: 100%;
  margin-top: 10px;
}
.btn-custom {
  padding: 0.5rem 1.5rem;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #2ecc71;
  color: white;
  font-size: large;
}

.container {
  margin-top: 40px; 
}
.main-title {
  color: #2ecc71;
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 2rem;
  opacity: 0;
  animation: typing 1s ease-in-out forwards;
}

.sub-title {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 30px;
  opacity: 0;
  animation: fadeIn 1s ease-in-out 1s forwards;
}


@keyframes typing {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (min-width: 768px) {
  #map {
    height: calc(70vh); /* 화면 높이에 맞춤 */
  }
}
</style>
