# 🛠️ 2025-10-25 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes 사용 시 흔히 저지르는 7가지 실수와 이를 피하는 방법에 대해 설명합니다. Kubernetes는 강력하지만 다루기 어려운 면이 있으며, 글쓴이는 자신과 다른 사람들이 겪은 실수들을 바탕으로 핵심적인 실수들을 정리하고 이를 피하는 팁을 공유합니다. 주요 내용은 다음과 같습니다:

1. **리소스 요청 및 제한 설정 건너뛰기**: Pod의 CPU 및 메모리 요구 사항을 명시하지 않으면 리소스 부족이나 과도한 리소스 소비로 인한 문제 발생 가능.
2. **활성 및 준비 상태 프로브 과소평가**: 컨테이너의 상태를 확인하는 프로브들을 설정하지 않으면, 비정상적인 상태에서의 문제를 감지하기 어려움.
3. **컨테이너 로그에만 의존하기**: `kubectl logs` 명령어에만 의존할 경우 로그 손실 위험이 있음. 중앙 집중화된 로그 관리 필요.
4. **개발환경과 운영환경을 동일하게 취급**: 환경별로 다른 요구 사항을 고려하지 않으면 성능 및 보안 문제 발생 가능.
5. **오래된 리소스 방치**: 오래된 리소스를 제거하지 않으면 불필요한 비용 발생 및 운영상의 혼란 초래.
6. **네트워킹에 너무 깊이 들어가기**: Kubernetes의 기본 네트워킹을 완전히 이해하기 전에 복잡한 네트워킹 솔루션을 도입하면 문제 해결이 어려움.
7. **보안 및 RBAC 설정 가볍게 처리**: 보안 설정을 소홀히 하면 보안 취약점 발생 가능성 증가.

글쓴이는 이러한 실수를 피하기 위한 구체적인 방법을 제시하고 있으며, Kubernetes를 더 깊이 이해하기 위해 공식 문서 및 커뮤니티 리소스를 활용할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Shell 4.0.0-M1 is available!
Spring Shell 4.0.0-M1 버전이 Maven Central에 출시되었습니다. 이 첫 마일스톤 릴리스는 Spring Shell의 현대화된 버전으로, Spring Framework 7 및 Spring Boot 4와의 정렬이 주요 목표입니다. Spring Shell 4.0.0-M1은 Spring Framework 7.0.0-RC2와 Spring Boot 4.0.0-RC1을 기반으로 합니다. 향후 계획으로는 11월에 Spring Boot 4.0 GA 릴리스 후 Spring Shell 4.0 GA를 출시할 예정이며, 그 전까지 몇 가지 마일스톤과 릴리스 후보가 제공될 것입니다. 주요 변경 사항으로는 jSpecify로의 널 가능성 주석 및 검사 이전, 프로젝트 모듈성 개선, JUnit 6로의 테스트 인프라 업데이트, 빌드 및 릴리스 인프라 개선, 문서 개선 등이 포함됩니다. 피드백은 GitHub Issues와 GitHub Discussions를 통해 받을 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/24/spring-shell-4-0-0-m1-released)

## 🔹 Docker - Docker Hub Incident Report – October 20, 2025
2025년 10월 20일, AWS의 US-East-1 지역에서 발생한 대규모 장애로 인해 Docker Hub에 심각한 서비스 중단이 발생했습니다. 전 세계 개발자들이 Docker를 일상적인 작업에 사용하고 있어 이번 중단은 큰 영향을 미쳤습니다. Docker는 이번 사건의 경과와 배운 점, 그리고 향후 시스템 강화를 위한 계획을 투명하게 공유하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-hub-incident-report-october-20-2025/)

## 🔹 Java - NUMA-Aware Relocation in ZGC
제목: ZGC의 NUMA 인식 재배치

요약: 최근 OpenJDK의 가비지 컬렉터 중 하나인 ZGC에 NUMA 인식 재배치 기능이 추가되었으며, JDK-8359683을 통해 JDK 26에 출시될 예정입니다. 최근의 메모리 할당 개편을 기반으로 이 기능은 ZGC의 NUMA 지원 및 최적화를 더욱 향상시킵니다.
👉 [자세히 보기](https://inside.java/2025/10/24/zgc-numa-aware-relocation/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25는 새로운 진단 도구인 '플라이트 레코딩'을 도입했습니다. 이 도구는 애플리케이션 실행 중 발생하는 다양한 이벤트를 기록하여 문제 해결에 도움을 줍니다. '플라이트 레코딩'은 실행 중인 프로그램의 상태를 분석하는 데 유용한 정보를 제공하여 개발자가 더 효과적으로 디버깅할 수 있도록 지원합니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"에서는 Helm의 10주년을 기념하며, Helm이 처음 탄생한 이야기를 다루고 있습니다. Helm은 10년 전, Kubernetes 1.1.0이 출시된 직후의 해커톤에서 처음 개발되었습니다. 최초 커밋은 2015년 10월 19일에 이루어졌으며, 이는 Helm이 Kubernetes 프로젝트와 통합되기 전의 초기 버전이었습니다. Helm의 첫 코드베이스는 helm-classic Git 저장소에서 찾을 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

