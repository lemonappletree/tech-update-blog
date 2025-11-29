# 🛠️ 2025-11-29 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
Kubernetes v1.35의 출시를 앞두고, Kubernetes 프로젝트는 발전을 계속하고 있습니다. 이번 블로그 글에서는 v1.35 릴리스에서 계획된 변경 사항을 설명하며, 클러스터 운영에 영향을 미칠 수 있는 주요 사항들을 다루고 있습니다.

1. **기능 제거 및 구식화**:
   - **cgroup v1 지원 제거**: cgroup v2의 도입으로 더 이상 cgroup v1을 지원하지 않습니다. 이는 구형 리눅스 배포판에서 영향을 미칠 수 있습니다.
   - **kube-proxy의 ipvs 모드 구식화**: 성능 향상을 위해 도입되었던 ipvs 모드가 기술적 복잡성과 기술 부채 문제로 인해 구식화됩니다.
   - **containerd v1.y 지원 구식화**: v1.35는 containerd 1.7 및 그 이하 버전에 대한 마지막 지원을 제공합니다.

2. **주요 기능 개선**:
   - **노드 선언 기능**: 노드가 지원하는 기능을 선언하여 스케줄링 정확도를 높이고 충돌을 방지합니다.
   - **Pod 자원 인플레이스 업데이트**: Pod를 재시작하지 않고 CPU와 메모리 자원을 조정할 수 있습니다.
   - **Pod 인증서**: Pod 간의 안전한 통신을 위해 자체 인증서를 제공하여 복잡한 외부 도구의 의존성을 줄입니다.
   - **수치적 Taints 지원**: Taints와 Tolerations에 수치 비교 연산자를 도입하여 보다 세밀한 스케줄링이 가능해집니다.
   - **사용자 네임스페이스**: 컨테이너의 root 사용자를 호스트에서 비특권 사용자로 매핑하여 보안을 강화합니다.
   - **OCI 이미지 볼륨 지원**: OCI 레지스트리에서 데이터를 직접 볼륨으로 마운트할 수 있게 하여 데이터 관리가 용이해집니다.

Kubernetes v1.35 릴리스는 2025년 12월 17일로 예정되어 있으며, 새로운 기능과 구식화된 사항들은 릴리스 노트를 통해 공식 발표될 예정입니다. 프로젝트에 참여하거나 최신 정보를 얻고 싶다면 Kubernetes 커뮤니티 모임에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
이 블로그 글은 Spring Tools 5의 새로운 기능인 '구조적 뷰'와 '고정관념(stereotype)'을 소개합니다. 개발자들이 Spring 프로젝트를 작업할 때 클래스나 인터페이스와 같은 저수준 개념뿐만 아니라 서비스, 저장소, 구성 클래스 등 고수준 추상화 개념을 사용합니다. Spring Tools는 이러한 개념을 중심으로 소스 코드를 분석하여 빠른 탐색과 개요를 제공합니다.

기존에는 "Go To Symbol" 기능을 통해 이러한 Spring 개념을 심볼로 만들어 제공했지만, 이번 주요 업데이트에서는 jMolecules 2.0과 협력하여 고정관념을 기반으로 한 논리적 구조 뷰를 제공합니다. 이 뷰는 프로젝트의 요소를 고정관념별로 그룹화하여 보여주며, 개발자가 필요에 따라 표시할 고정관념 그룹을 선택할 수 있습니다. 또한, Spring Modulith를 사용하는 경우 모듈 구조도 자동으로 반영됩니다.

개발자는 자신만의 고정관념을 정의할 수 있으며, 이러한 정의는 Spring Tools가 자동으로 감지하여 논리적 구조 뷰에 반영합니다. Spring Tools 5의 최신 버전은 [도구 미리보기 페이지](https://spring.io/tools5)에서 사용할 수 있으며, 이후 AI 코딩 어시스턴트와의 통합에 대한 내용이 추가될 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - You Want Microservices, But Do You Really Need Them?
이 블로그 글은 마이크로서비스를 도입하려는 기업들에게 정말 필요한지 다시 생각해보라고 권고합니다. 2023년 5월, 아마존이 Prime Video 서비스에서 마이크로서비스를 포기하고 모놀리식 아키텍처로 전환하여 비용을 무려 90% 절감한 사례를 소개합니다. AWS로 마이크로서비스 인프라를 판매하며 막대한 수익을 올리는 아마존조차도 때때로 전통적인 모놀리식 구조가 더 나을 수 있음을 인정한 것입니다.
👉 [자세히 보기](https://www.docker.com/blog/do-you-really-need-microservices/)

## 🔹 Java - Help, My Java Object Vanished (and the GC is Not at Fault)
이 블로그 글은 Project Valhalla의 개발 과정을 소개하며, HotSpot의 내부 작동 방식에 대한 통찰을 제공합니다. 또한 JVM 플래그를 활용하여 문제를 해결하는 방법을 실용적으로 보여주며, HotSpot 디버깅 시 배운 교훈들을 공유합니다. Java 객체가 사라지는 문제와 관련해 가비지 컬렉터(GC)가 원인이 아님을 설명합니다.
👉 [자세히 보기](https://inside.java/2025/11/28/markword/)

## 🔹 Golang - Go’s Sweet 16
제목: Go의 16번째 생일

요약: Go 프로그래밍 언어의 16주년을 기념하는 글입니다. Go의 탄생을 축하하고, 그동안의 발전과 성과를 되돌아보며 앞으로의 가능성을 조망합니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
블로그 글 요약: 11월 12일 수요일, KubeCon + CloudNativeCon에서 열린 Helm 4 발표 중에 Helm v4.0.0이 출시되었습니다. 이는 6년 만에 발표된 Helm의 새로운 주요 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

