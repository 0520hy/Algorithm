function solution(participant, completion) {
   const participantMap = {}; // 참가자 이름과 개수를 저장할 객체

   // 참가자 이름과 개수를 카운트하여 participantMap에 저장
   for (let name of participant) {
      if (participantMap[name]) {
         participantMap[name]++;
      } else {
         participantMap[name] = 1;
      }
   }

   // 완주한 참가자 이름을 participantMap에서 개수를 감소시키며 제거
   for (let name of completion) {
      participantMap[name]--;
      if (participantMap[name] === 0) {
         delete participantMap[name];
      }
   }

   // participantMap에 남아있는 이름이 완주하지 못한 참가자
   const answer = Object.keys(participantMap)[0];
   return answer;
}
