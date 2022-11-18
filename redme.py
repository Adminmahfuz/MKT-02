Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@Adminmahfuz 
sabbir28
/
Unity
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Add files via upload
 main
@sabbir28
sabbir28 committed 18 days ago 
1 parent 82b115d commit fac4c58f995550cfffd92399cac7bd118e770779
Show file tree Hide file tree
Showing 40 changed files with 4,044 additions and 0 deletions.
Filter changed files
 33  
UnityEngine.UI/EventSystems/AbstractEventData.cs
@@ -0,0 +1,33 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000021 RID: 33
	public abstract class AbstractEventData
	{
		// Token: 0x06000093 RID: 147 RVA: 0x0000360E File Offset: 0x00001A0E
		public virtual void Reset()
		{
			this.m_Used = false;
		}

		// Token: 0x06000094 RID: 148 RVA: 0x00003618 File Offset: 0x00001A18
		public virtual void Use()
		{
			this.m_Used = true;
		}

		// Token: 0x17000020 RID: 32
		// (get) Token: 0x06000095 RID: 149 RVA: 0x00003624 File Offset: 0x00001A24
		public virtual bool used
		{
			get
			{
				return this.m_Used;
			}
		}

		// Token: 0x0400005D RID: 93
		protected bool m_Used;
	}
}
 25  
UnityEngine.UI/EventSystems/AxisEventData.cs
@@ -0,0 +1,25 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000020 RID: 32
	public class AxisEventData : BaseEventData
	{
		// Token: 0x0600008D RID: 141 RVA: 0x000036A0 File Offset: 0x00001AA0
		public AxisEventData(EventSystem eventSystem) : base(eventSystem)
		{
			this.moveVector = Vector2.zero;
			this.moveDir = MoveDirection.None;
		}

		// Token: 0x1700001E RID: 30
		// (get) Token: 0x0600008E RID: 142 RVA: 0x000036BC File Offset: 0x00001ABC
		// (set) Token: 0x0600008F RID: 143 RVA: 0x000036D6 File Offset: 0x00001AD6
		public Vector2 moveVector { get; set; }

		// Token: 0x1700001F RID: 31
		// (get) Token: 0x06000090 RID: 144 RVA: 0x000036E0 File Offset: 0x00001AE0
		// (set) Token: 0x06000091 RID: 145 RVA: 0x000036FA File Offset: 0x00001AFA
		public MoveDirection moveDir { get; set; }
	}
}
 42  
UnityEngine.UI/EventSystems/BaseEventData.cs
@@ -0,0 +1,42 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000022 RID: 34
	public class BaseEventData : AbstractEventData
	{
		// Token: 0x06000096 RID: 150 RVA: 0x0000363F File Offset: 0x00001A3F
		public BaseEventData(EventSystem eventSystem)
		{
			this.m_EventSystem = eventSystem;
		}

		// Token: 0x17000021 RID: 33
		// (get) Token: 0x06000097 RID: 151 RVA: 0x00003650 File Offset: 0x00001A50
		public BaseInputModule currentInputModule
		{
			get
			{
				return this.m_EventSystem.currentInputModule;
			}
		}

		// Token: 0x17000022 RID: 34
		// (get) Token: 0x06000098 RID: 152 RVA: 0x00003670 File Offset: 0x00001A70
		// (set) Token: 0x06000099 RID: 153 RVA: 0x00003690 File Offset: 0x00001A90
		public GameObject selectedObject
		{
			get
			{
				return this.m_EventSystem.currentSelectedGameObject;
			}
			set
			{
				this.m_EventSystem.SetSelectedGameObject(value, this);
			}
		}

		// Token: 0x0400005E RID: 94
		private readonly EventSystem m_EventSystem;
	}
}
 134  
UnityEngine.UI/EventSystems/BaseInput.cs
@@ -0,0 +1,134 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000026 RID: 38
	public class BaseInput : UIBehaviour
	{
		// Token: 0x17000039 RID: 57
		// (get) Token: 0x060000C9 RID: 201 RVA: 0x00003CA8 File Offset: 0x000020A8
		public virtual string compositionString
		{
			get
			{
				return Input.compositionString;
			}
		}

		// Token: 0x1700003A RID: 58
		// (get) Token: 0x060000CA RID: 202 RVA: 0x00003CC4 File Offset: 0x000020C4
		// (set) Token: 0x060000CB RID: 203 RVA: 0x00003CDE File Offset: 0x000020DE
		public virtual IMECompositionMode imeCompositionMode
		{
			get
			{
				return Input.imeCompositionMode;
			}
			set
			{
				Input.imeCompositionMode = value;
			}
		}

		// Token: 0x1700003B RID: 59
		// (get) Token: 0x060000CC RID: 204 RVA: 0x00003CE8 File Offset: 0x000020E8
		// (set) Token: 0x060000CD RID: 205 RVA: 0x00003D02 File Offset: 0x00002102
		public virtual Vector2 compositionCursorPos
		{
			get
			{
				return Input.compositionCursorPos;
			}
			set
			{
				Input.compositionCursorPos = value;
			}
		}

		// Token: 0x1700003C RID: 60
		// (get) Token: 0x060000CE RID: 206 RVA: 0x00003D0C File Offset: 0x0000210C
		public virtual bool mousePresent
		{
			get
			{
				return Input.mousePresent;
			}
		}

		// Token: 0x060000CF RID: 207 RVA: 0x00003D28 File Offset: 0x00002128
		public virtual bool GetMouseButtonDown(int button)
		{
			return Input.GetMouseButtonDown(button);
		}

		// Token: 0x060000D0 RID: 208 RVA: 0x00003D44 File Offset: 0x00002144
		public virtual bool GetMouseButtonUp(int button)
		{
			return Input.GetMouseButtonUp(button);
		}

		// Token: 0x060000D1 RID: 209 RVA: 0x00003D60 File Offset: 0x00002160
		public virtual bool GetMouseButton(int button)
		{
			return Input.GetMouseButton(button);
		}

		// Token: 0x1700003D RID: 61
		// (get) Token: 0x060000D2 RID: 210 RVA: 0x00003D7C File Offset: 0x0000217C
		public virtual Vector2 mousePosition
		{
			get
			{
				return Input.mousePosition;
			}
		}

		// Token: 0x1700003E RID: 62
		// (get) Token: 0x060000D3 RID: 211 RVA: 0x00003D9C File Offset: 0x0000219C
		public virtual Vector2 mouseScrollDelta
		{
			get
			{
				return Input.mouseScrollDelta;
			}
		}

		// Token: 0x1700003F RID: 63
		// (get) Token: 0x060000D4 RID: 212 RVA: 0x00003DB8 File Offset: 0x000021B8
		public virtual bool touchSupported
		{
			get
			{
				return Input.touchSupported;
			}
		}

		// Token: 0x17000040 RID: 64
		// (get) Token: 0x060000D5 RID: 213 RVA: 0x00003DD4 File Offset: 0x000021D4
		public virtual int touchCount
		{
			get
			{
				return Input.touchCount;
			}
		}

		// Token: 0x060000D6 RID: 214 RVA: 0x00003DF0 File Offset: 0x000021F0
		public virtual Touch GetTouch(int index)
		{
			return Input.GetTouch(index);
		}

		// Token: 0x060000D7 RID: 215 RVA: 0x00003E0C File Offset: 0x0000220C
		public virtual float GetAxisRaw(string axisName)
		{
			return Input.GetAxisRaw(axisName);
		}

		// Token: 0x060000D8 RID: 216 RVA: 0x00003E28 File Offset: 0x00002228
		public virtual bool GetButtonDown(string buttonName)
		{
			return Input.GetButtonDown(buttonName);
		}
	}
}
 275  
UnityEngine.UI/EventSystems/BaseInputModule.cs
@@ -0,0 +1,275 @@
using System;
using System.Collections.Generic;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000027 RID: 39
	[RequireComponent(typeof(EventSystem))]
	public abstract class BaseInputModule : UIBehaviour
	{
		// Token: 0x17000041 RID: 65
		// (get) Token: 0x060000DA RID: 218 RVA: 0x00003E58 File Offset: 0x00002258
		public BaseInput input
		{
			get
			{
				BaseInput result;
				if (this.m_InputOverride != null)
				{
					result = this.m_InputOverride;
				}
				else
				{
					if (this.m_DefaultInput == null)
					{
						BaseInput[] components = base.GetComponents<BaseInput>();
						foreach (BaseInput baseInput in components)
						{
							if (baseInput != null && baseInput.GetType() == typeof(BaseInput))
							{
								this.m_DefaultInput = baseInput;
								break;
							}
						}
						if (this.m_DefaultInput == null)
						{
							this.m_DefaultInput = base.gameObject.AddComponent<BaseInput>();
						}
					}
					result = this.m_DefaultInput;
				}
				return result;
			}
		}

		// Token: 0x17000042 RID: 66
		// (get) Token: 0x060000DB RID: 219 RVA: 0x00003F1C File Offset: 0x0000231C
		protected EventSystem eventSystem
		{
			get
			{
				return this.m_EventSystem;
			}
		}

		// Token: 0x060000DC RID: 220 RVA: 0x00003F37 File Offset: 0x00002337
		protected override void OnEnable()
		{
			base.OnEnable();
			this.m_EventSystem = base.GetComponent<EventSystem>();
			this.m_EventSystem.UpdateModules();
		}

		// Token: 0x060000DD RID: 221 RVA: 0x00003F57 File Offset: 0x00002357
		protected override void OnDisable()
		{
			this.m_EventSystem.UpdateModules();
			base.OnDisable();
		}

		// Token: 0x060000DE RID: 222
		public abstract void Process();

		// Token: 0x060000DF RID: 223 RVA: 0x00003F6C File Offset: 0x0000236C
		protected static RaycastResult FindFirstRaycast(List<RaycastResult> candidates)
		{
			for (int i = 0; i < candidates.Count; i++)
			{
				if (!(candidates[i].gameObject == null))
				{
					return candidates[i];
				}
			}
			return default(RaycastResult);
		}

		// Token: 0x060000E0 RID: 224 RVA: 0x00003FD0 File Offset: 0x000023D0
		protected static MoveDirection DetermineMoveDirection(float x, float y)
		{
			return BaseInputModule.DetermineMoveDirection(x, y, 0.6f);
		}

		// Token: 0x060000E1 RID: 225 RVA: 0x00003FF4 File Offset: 0x000023F4
		protected static MoveDirection DetermineMoveDirection(float x, float y, float deadZone)
		{
			Vector2 vector = new Vector2(x, y);
			MoveDirection result;
			if (vector.sqrMagnitude < deadZone * deadZone)
			{
				result = MoveDirection.None;
			}
			else if (Mathf.Abs(x) > Mathf.Abs(y))
			{
				if (x > 0f)
				{
					result = MoveDirection.Right;
				}
				else
				{
					result = MoveDirection.Left;
				}
			}
			else if (y > 0f)
			{
				result = MoveDirection.Up;
			}
			else
			{
				result = MoveDirection.Down;
			}
			return result;
		}

		// Token: 0x060000E2 RID: 226 RVA: 0x00004068 File Offset: 0x00002468
		protected static GameObject FindCommonRoot(GameObject g1, GameObject g2)
		{
			GameObject result;
			if (g1 == null || g2 == null)
			{
				result = null;
			}
			else
			{
				Transform transform = g1.transform;
				while (transform != null)
				{
					Transform transform2 = g2.transform;
					while (transform2 != null)
					{
						if (transform == transform2)
						{
							return transform.gameObject;
						}
						transform2 = transform2.parent;
					}
					transform = transform.parent;
				}
				result = null;
			}
			return result;
		}

		// Token: 0x060000E3 RID: 227 RVA: 0x000040F8 File Offset: 0x000024F8
		protected void HandlePointerExitAndEnter(PointerEventData currentPointerData, GameObject newEnterTarget)
		{
			if (newEnterTarget == null || currentPointerData.pointerEnter == null)
			{
				for (int i = 0; i < currentPointerData.hovered.Count; i++)
				{
					ExecuteEvents.Execute<IPointerExitHandler>(currentPointerData.hovered[i], currentPointerData, ExecuteEvents.pointerExitHandler);
				}
				currentPointerData.hovered.Clear();
				if (newEnterTarget == null)
				{
					currentPointerData.pointerEnter = newEnterTarget;
					return;
				}
			}
			if (!(currentPointerData.pointerEnter == newEnterTarget) || !newEnterTarget)
			{
				GameObject gameObject = BaseInputModule.FindCommonRoot(currentPointerData.pointerEnter, newEnterTarget);
				if (currentPointerData.pointerEnter != null)
				{
					Transform transform = currentPointerData.pointerEnter.transform;
					while (transform != null)
					{
						if (gameObject != null && gameObject.transform == transform)
						{
							break;
						}
						ExecuteEvents.Execute<IPointerExitHandler>(transform.gameObject, currentPointerData, ExecuteEvents.pointerExitHandler);
						currentPointerData.hovered.Remove(transform.gameObject);
						transform = transform.parent;
					}
				}
				currentPointerData.pointerEnter = newEnterTarget;
				if (newEnterTarget != null)
				{
					Transform transform2 = newEnterTarget.transform;
					while (transform2 != null && transform2.gameObject != gameObject)
					{
						ExecuteEvents.Execute<IPointerEnterHandler>(transform2.gameObject, currentPointerData, ExecuteEvents.pointerEnterHandler);
						currentPointerData.hovered.Add(transform2.gameObject);
						transform2 = transform2.parent;
					}
				}
			}
		}

		// Token: 0x060000E4 RID: 228 RVA: 0x00004294 File Offset: 0x00002694
		protected virtual AxisEventData GetAxisEventData(float x, float y, float moveDeadZone)
		{
			if (this.m_AxisEventData == null)
			{
				this.m_AxisEventData = new AxisEventData(this.eventSystem);
			}
			this.m_AxisEventData.Reset();
			this.m_AxisEventData.moveVector = new Vector2(x, y);
			this.m_AxisEventData.moveDir = BaseInputModule.DetermineMoveDirection(x, y, moveDeadZone);
			return this.m_AxisEventData;
		}

		// Token: 0x060000E5 RID: 229 RVA: 0x000042FC File Offset: 0x000026FC
		protected virtual BaseEventData GetBaseEventData()
		{
			if (this.m_BaseEventData == null)
			{
				this.m_BaseEventData = new BaseEventData(this.eventSystem);
			}
			this.m_BaseEventData.Reset();
			return this.m_BaseEventData;
		}

		// Token: 0x060000E6 RID: 230 RVA: 0x00004340 File Offset: 0x00002740
		public virtual bool IsPointerOverGameObject(int pointerId)
		{
			return false;
		}

		// Token: 0x060000E7 RID: 231 RVA: 0x00004358 File Offset: 0x00002758
		public virtual bool ShouldActivateModule()
		{
			return base.enabled && base.gameObject.activeInHierarchy;
		}

		// Token: 0x060000E8 RID: 232 RVA: 0x00004386 File Offset: 0x00002786
		public virtual void DeactivateModule()
		{
		}

		// Token: 0x060000E9 RID: 233 RVA: 0x00004389 File Offset: 0x00002789
		public virtual void ActivateModule()
		{
		}

		// Token: 0x060000EA RID: 234 RVA: 0x0000438C File Offset: 0x0000278C
		public virtual void UpdateModule()
		{
		}

		// Token: 0x060000EB RID: 235 RVA: 0x00004390 File Offset: 0x00002790
		public virtual bool IsModuleSupported()
		{
			return true;
		}

		// Token: 0x0400007D RID: 125
		[NonSerialized]
		protected List<RaycastResult> m_RaycastResultCache = new List<RaycastResult>();

		// Token: 0x0400007E RID: 126
		private AxisEventData m_AxisEventData;

		// Token: 0x0400007F RID: 127
		private EventSystem m_EventSystem;

		// Token: 0x04000080 RID: 128
		private BaseEventData m_BaseEventData;

		// Token: 0x04000081 RID: 129
		protected BaseInput m_InputOverride;

		// Token: 0x04000082 RID: 130
		private BaseInput m_DefaultInput;
	}
}
 77  
UnityEngine.UI/EventSystems/BaseRaycaster.cs
@@ -0,0 +1,77 @@
using System;
using System.Collections.Generic;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200002F RID: 47
	public abstract class BaseRaycaster : UIBehaviour
	{
		// Token: 0x0600013C RID: 316
		public abstract void Raycast(PointerEventData eventData, List<RaycastResult> resultAppendList);

		// Token: 0x17000050 RID: 80
		// (get) Token: 0x0600013D RID: 317
		public abstract Camera eventCamera { get; }

		// Token: 0x17000051 RID: 81
		// (get) Token: 0x0600013E RID: 318 RVA: 0x00006030 File Offset: 0x00004430
		[Obsolete("Please use sortOrderPriority and renderOrderPriority", false)]
		public virtual int priority
		{
			get
			{
				return 0;
			}
		}

		// Token: 0x17000052 RID: 82
		// (get) Token: 0x0600013F RID: 319 RVA: 0x00006048 File Offset: 0x00004448
		public virtual int sortOrderPriority
		{
			get
			{
				return int.MinValue;
			}
		}

		// Token: 0x17000053 RID: 83
		// (get) Token: 0x06000140 RID: 320 RVA: 0x00006064 File Offset: 0x00004464
		public virtual int renderOrderPriority
		{
			get
			{
				return int.MinValue;
			}
		}

		// Token: 0x06000141 RID: 321 RVA: 0x00006080 File Offset: 0x00004480
		public override string ToString()
		{
			return string.Concat(new object[]
			{
				"Name: ",
				base.gameObject,
				"\neventCamera: ",
				this.eventCamera,
				"\nsortOrderPriority: ",
				this.sortOrderPriority,
				"\nrenderOrderPriority: ",
				this.renderOrderPriority
			});
		}

		// Token: 0x06000142 RID: 322 RVA: 0x000060EE File Offset: 0x000044EE
		protected override void OnEnable()
		{
			base.OnEnable();
			RaycasterManager.AddRaycaster(this);
		}

		// Token: 0x06000143 RID: 323 RVA: 0x000060FD File Offset: 0x000044FD
		protected override void OnDisable()
		{
			RaycasterManager.RemoveRaycasters(this);
			base.OnDisable();
		}
	}
}
 14  
UnityEngine.UI/EventSystems/EventHandle.cs
@@ -0,0 +1,14 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000002 RID: 2
	[Flags]
	public enum EventHandle
	{
		// Token: 0x04000002 RID: 2
		Unused = 0,
		// Token: 0x04000003 RID: 3
		Used = 1
	}
}
 412  
UnityEngine.UI/EventSystems/EventSystem.cs
Large diffs are not rendered by default.

 180  
UnityEngine.UI/EventSystems/EventTrigger.cs
@@ -0,0 +1,180 @@
using System;
using System.Collections.Generic;
using UnityEngine.Events;
using UnityEngine.Serialization;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000016 RID: 22
	[AddComponentMenu("Event/Event Trigger")]
	public class EventTrigger : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerDownHandler, IPointerUpHandler, IPointerClickHandler, IInitializePotentialDragHandler, IBeginDragHandler, IDragHandler, IEndDragHandler, IDropHandler, IScrollHandler, IUpdateSelectedHandler, ISelectHandler, IDeselectHandler, IMoveHandler, ISubmitHandler, ICancelHandler, IEventSystemHandler
	{
		// Token: 0x0600002F RID: 47 RVA: 0x0000292B File Offset: 0x00000D2B
		protected EventTrigger()
		{
		}

		// Token: 0x1700000A RID: 10
		// (get) Token: 0x06000030 RID: 48 RVA: 0x00002934 File Offset: 0x00000D34
		// (set) Token: 0x06000031 RID: 49 RVA: 0x00002965 File Offset: 0x00000D65
		public List<EventTrigger.Entry> triggers
		{
			get
			{
				if (this.m_Delegates == null)
				{
					this.m_Delegates = new List<EventTrigger.Entry>();
				}
				return this.m_Delegates;
			}
			set
			{
				this.m_Delegates = value;
			}
		}

		// Token: 0x06000032 RID: 50 RVA: 0x00002970 File Offset: 0x00000D70
		private void Execute(EventTriggerType id, BaseEventData eventData)
		{
			int i = 0;
			int count = this.triggers.Count;
			while (i < count)
			{
				EventTrigger.Entry entry = this.triggers[i];
				if (entry.eventID == id && entry.callback != null)
				{
					entry.callback.Invoke(eventData);
				}
				i++;
			}
		}

		// Token: 0x06000033 RID: 51 RVA: 0x000029CE File Offset: 0x00000DCE
		public virtual void OnPointerEnter(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.PointerEnter, eventData);
		}

		// Token: 0x06000034 RID: 52 RVA: 0x000029D9 File Offset: 0x00000DD9
		public virtual void OnPointerExit(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.PointerExit, eventData);
		}

		// Token: 0x06000035 RID: 53 RVA: 0x000029E4 File Offset: 0x00000DE4
		public virtual void OnDrag(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.Drag, eventData);
		}

		// Token: 0x06000036 RID: 54 RVA: 0x000029EF File Offset: 0x00000DEF
		public virtual void OnDrop(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.Drop, eventData);
		}

		// Token: 0x06000037 RID: 55 RVA: 0x000029FA File Offset: 0x00000DFA
		public virtual void OnPointerDown(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.PointerDown, eventData);
		}

		// Token: 0x06000038 RID: 56 RVA: 0x00002A05 File Offset: 0x00000E05
		public virtual void OnPointerUp(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.PointerUp, eventData);
		}

		// Token: 0x06000039 RID: 57 RVA: 0x00002A10 File Offset: 0x00000E10
		public virtual void OnPointerClick(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.PointerClick, eventData);
		}

		// Token: 0x0600003A RID: 58 RVA: 0x00002A1B File Offset: 0x00000E1B
		public virtual void OnSelect(BaseEventData eventData)
		{
			this.Execute(EventTriggerType.Select, eventData);
		}

		// Token: 0x0600003B RID: 59 RVA: 0x00002A27 File Offset: 0x00000E27
		public virtual void OnDeselect(BaseEventData eventData)
		{
			this.Execute(EventTriggerType.Deselect, eventData);
		}

		// Token: 0x0600003C RID: 60 RVA: 0x00002A33 File Offset: 0x00000E33
		public virtual void OnScroll(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.Scroll, eventData);
		}

		// Token: 0x0600003D RID: 61 RVA: 0x00002A3E File Offset: 0x00000E3E
		public virtual void OnMove(AxisEventData eventData)
		{
			this.Execute(EventTriggerType.Move, eventData);
		}

		// Token: 0x0600003E RID: 62 RVA: 0x00002A4A File Offset: 0x00000E4A
		public virtual void OnUpdateSelected(BaseEventData eventData)
		{
			this.Execute(EventTriggerType.UpdateSelected, eventData);
		}

		// Token: 0x0600003F RID: 63 RVA: 0x00002A55 File Offset: 0x00000E55
		public virtual void OnInitializePotentialDrag(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.InitializePotentialDrag, eventData);
		}

		// Token: 0x06000040 RID: 64 RVA: 0x00002A61 File Offset: 0x00000E61
		public virtual void OnBeginDrag(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.BeginDrag, eventData);
		}

		// Token: 0x06000041 RID: 65 RVA: 0x00002A6D File Offset: 0x00000E6D
		public virtual void OnEndDrag(PointerEventData eventData)
		{
			this.Execute(EventTriggerType.EndDrag, eventData);
		}

		// Token: 0x06000042 RID: 66 RVA: 0x00002A79 File Offset: 0x00000E79
		public virtual void OnSubmit(BaseEventData eventData)
		{
			this.Execute(EventTriggerType.Submit, eventData);
		}

		// Token: 0x06000043 RID: 67 RVA: 0x00002A85 File Offset: 0x00000E85
		public virtual void OnCancel(BaseEventData eventData)
		{
			this.Execute(EventTriggerType.Cancel, eventData);
		}

		// Token: 0x04000010 RID: 16
		[FormerlySerializedAs("delegates")]
		[SerializeField]
		private List<EventTrigger.Entry> m_Delegates;

		// Token: 0x04000011 RID: 17
		[Obsolete("Please use triggers instead (UnityUpgradable) -> triggers", true)]
		public List<EventTrigger.Entry> delegates;

		// Token: 0x02000017 RID: 23
		[Serializable]
		public class TriggerEvent : UnityEvent<BaseEventData>
		{
		}

		// Token: 0x02000018 RID: 24
		[Serializable]
		public class Entry
		{
			// Token: 0x04000012 RID: 18
			public EventTriggerType eventID = EventTriggerType.PointerClick;

			// Token: 0x04000013 RID: 19
			public EventTrigger.TriggerEvent callback = new EventTrigger.TriggerEvent();
		}
	}
}
 43  
UnityEngine.UI/EventSystems/EventTriggerType.cs
@@ -0,0 +1,43 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000019 RID: 25
	public enum EventTriggerType
	{
		// Token: 0x04000015 RID: 21
		PointerEnter,
		// Token: 0x04000016 RID: 22
		PointerExit,
		// Token: 0x04000017 RID: 23
		PointerDown,
		// Token: 0x04000018 RID: 24
		PointerUp,
		// Token: 0x04000019 RID: 25
		PointerClick,
		// Token: 0x0400001A RID: 26
		Drag,
		// Token: 0x0400001B RID: 27
		Drop,
		// Token: 0x0400001C RID: 28
		Scroll,
		// Token: 0x0400001D RID: 29
		UpdateSelected,
		// Token: 0x0400001E RID: 30
		Select,
		// Token: 0x0400001F RID: 31
		Deselect,
		// Token: 0x04000020 RID: 32
		Move,
		// Token: 0x04000021 RID: 33
		InitializePotentialDrag,
		// Token: 0x04000022 RID: 34
		BeginDrag,
		// Token: 0x04000023 RID: 35
		EndDrag,
		// Token: 0x04000024 RID: 36
		Submit,
		// Token: 0x04000025 RID: 37
		Cancel
	}
}
 659  
UnityEngine.UI/EventSystems/ExecuteEvents.cs
Large diffs are not rendered by default.

 11  
UnityEngine.UI/EventSystems/IBeginDragHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000009 RID: 9
	public interface IBeginDragHandler : IEventSystemHandler
	{
		// Token: 0x06000006 RID: 6
		void OnBeginDrag(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/ICancelHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000014 RID: 20
	public interface ICancelHandler : IEventSystemHandler
	{
		// Token: 0x06000011 RID: 17
		void OnCancel(BaseEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IDeselectHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000011 RID: 17
	public interface IDeselectHandler : IEventSystemHandler
	{
		// Token: 0x0600000E RID: 14
		void OnDeselect(BaseEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IDragHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000B RID: 11
	public interface IDragHandler : IEventSystemHandler
	{
		// Token: 0x06000008 RID: 8
		void OnDrag(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IDropHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000D RID: 13
	public interface IDropHandler : IEventSystemHandler
	{
		// Token: 0x0600000A RID: 10
		void OnDrop(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IEndDragHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000C RID: 12
	public interface IEndDragHandler : IEventSystemHandler
	{
		// Token: 0x06000009 RID: 9
		void OnEndDrag(PointerEventData eventData);
	}
}
 9  
UnityEngine.UI/EventSystems/IEventSystemHandler.cs
@@ -0,0 +1,9 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000003 RID: 3
	public interface IEventSystemHandler
	{
	}
}
 11  
UnityEngine.UI/EventSystems/IInitializePotentialDragHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000A RID: 10
	public interface IInitializePotentialDragHandler : IEventSystemHandler
	{
		// Token: 0x06000007 RID: 7
		void OnInitializePotentialDrag(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IMoveHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000012 RID: 18
	public interface IMoveHandler : IEventSystemHandler
	{
		// Token: 0x0600000F RID: 15
		void OnMove(AxisEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IPointerClickHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000008 RID: 8
	public interface IPointerClickHandler : IEventSystemHandler
	{
		// Token: 0x06000005 RID: 5
		void OnPointerClick(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IPointerDownHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000006 RID: 6
	public interface IPointerDownHandler : IEventSystemHandler
	{
		// Token: 0x06000003 RID: 3
		void OnPointerDown(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IPointerEnterHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000004 RID: 4
	public interface IPointerEnterHandler : IEventSystemHandler
	{
		// Token: 0x06000001 RID: 1
		void OnPointerEnter(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IPointerExitHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000005 RID: 5
	public interface IPointerExitHandler : IEventSystemHandler
	{
		// Token: 0x06000002 RID: 2
		void OnPointerExit(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IPointerUpHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000007 RID: 7
	public interface IPointerUpHandler : IEventSystemHandler
	{
		// Token: 0x06000004 RID: 4
		void OnPointerUp(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IScrollHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000E RID: 14
	public interface IScrollHandler : IEventSystemHandler
	{
		// Token: 0x0600000B RID: 11
		void OnScroll(PointerEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/ISelectHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000010 RID: 16
	public interface ISelectHandler : IEventSystemHandler
	{
		// Token: 0x0600000D RID: 13
		void OnSelect(BaseEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/ISubmitHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000013 RID: 19
	public interface ISubmitHandler : IEventSystemHandler
	{
		// Token: 0x06000010 RID: 16
		void OnSubmit(BaseEventData eventData);
	}
}
 11  
UnityEngine.UI/EventSystems/IUpdateSelectedHandler.cs
@@ -0,0 +1,11 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200000F RID: 15
	public interface IUpdateSelectedHandler : IEventSystemHandler
	{
		// Token: 0x0600000C RID: 12
		void OnUpdateSelected(BaseEventData eventData);
	}
}
 19  
UnityEngine.UI/EventSystems/MoveDirection.cs
@@ -0,0 +1,19 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200001C RID: 28
	public enum MoveDirection
	{
		// Token: 0x0400004B RID: 75
		Left,
		// Token: 0x0400004C RID: 76
		Up,
		// Token: 0x0400004D RID: 77
		Right,
		// Token: 0x0400004E RID: 78
		Down,
		// Token: 0x0400004F RID: 79
		None
	}
}
 55  
UnityEngine.UI/EventSystems/Physics2DRaycaster.cs
@@ -0,0 +1,55 @@
using System;
using System.Collections.Generic;
using UnityEngine.UI;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000030 RID: 48
	[AddComponentMenu("Event/Physics 2D Raycaster")]
	[RequireComponent(typeof(Camera))]
	public class Physics2DRaycaster : PhysicsRaycaster
	{
		// Token: 0x06000144 RID: 324 RVA: 0x000063F2 File Offset: 0x000047F2
		protected Physics2DRaycaster()
		{
		}

		// Token: 0x06000145 RID: 325 RVA: 0x000063FC File Offset: 0x000047FC
		public override void Raycast(PointerEventData eventData, List<RaycastResult> resultAppendList)
		{
			if (!(this.eventCamera == null))
			{
				Ray r;
				float f;
				base.ComputeRayAndDistance(eventData, out r, out f);
				if (ReflectionMethodsCache.Singleton.getRayIntersectionAll != null)
				{
					RaycastHit2D[] array = ReflectionMethodsCache.Singleton.getRayIntersectionAll(r, f, base.finalEventMask);
					if (array.Length != 0)
					{
						int i = 0;
						int num = array.Length;
						while (i < num)
						{
							SpriteRenderer component = array[i].collider.gameObject.GetComponent<SpriteRenderer>();
							RaycastResult item = new RaycastResult
							{
								gameObject = array[i].collider.gameObject,
								module = this,
								distance = Vector3.Distance(this.eventCamera.transform.position, array[i].point),
								worldPosition = array[i].point,
								worldNormal = array[i].normal,
								screenPosition = eventData.position,
								index = (float)resultAppendList.Count,
								sortingLayer = ((!(component != null)) ? 0 : component.sortingLayerID),
								sortingOrder = ((!(component != null)) ? 0 : component.sortingOrder)
							};
							resultAppendList.Add(item);
							i++;
						}
					}
				}
			}
		}
	}
}
 125  
UnityEngine.UI/EventSystems/PhysicsRaycaster.cs
@@ -0,0 +1,125 @@
using System;
using System.Collections.Generic;
using UnityEngine.UI;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000031 RID: 49
	[AddComponentMenu("Event/Physics Raycaster")]
	[RequireComponent(typeof(Camera))]
	public class PhysicsRaycaster : BaseRaycaster
	{
		// Token: 0x06000146 RID: 326 RVA: 0x0000610C File Offset: 0x0000450C
		protected PhysicsRaycaster()
		{
		}

		// Token: 0x17000054 RID: 84
		// (get) Token: 0x06000147 RID: 327 RVA: 0x00006124 File Offset: 0x00004524
		public override Camera eventCamera
		{
			get
			{
				if (this.m_EventCamera == null)
				{
					this.m_EventCamera = base.GetComponent<Camera>();
				}
				return this.m_EventCamera ?? Camera.main;
			}
		}

		// Token: 0x17000055 RID: 85
		// (get) Token: 0x06000148 RID: 328 RVA: 0x00006168 File Offset: 0x00004568
		public virtual int depth
		{
			get
			{
				return (!(this.eventCamera != null)) ? 16777215 : ((int)this.eventCamera.depth);
			}
		}

		// Token: 0x17000056 RID: 86
		// (get) Token: 0x06000149 RID: 329 RVA: 0x000061A4 File Offset: 0x000045A4
		public int finalEventMask
		{
			get
			{
				return (!(this.eventCamera != null)) ? -1 : (this.eventCamera.cullingMask & this.m_EventMask);
			}
		}

		// Token: 0x17000057 RID: 87
		// (get) Token: 0x0600014A RID: 330 RVA: 0x000061E8 File Offset: 0x000045E8
		// (set) Token: 0x0600014B RID: 331 RVA: 0x00006203 File Offset: 0x00004603
		public LayerMask eventMask
		{
			get
			{
				return this.m_EventMask;
			}
			set
			{
				this.m_EventMask = value;
			}
		}

		// Token: 0x0600014C RID: 332 RVA: 0x00006210 File Offset: 0x00004610
		protected void ComputeRayAndDistance(PointerEventData eventData, out Ray ray, out float distanceToClipPlane)
		{
			ray = this.eventCamera.ScreenPointToRay(eventData.position);
			float z = ray.direction.z;
			distanceToClipPlane = ((!Mathf.Approximately(0f, z)) ? Mathf.Abs((this.eventCamera.farClipPlane - this.eventCamera.nearClipPlane) / z) : float.PositiveInfinity);
		}

		// Token: 0x0600014D RID: 333 RVA: 0x00006284 File Offset: 0x00004684
		public override void Raycast(PointerEventData eventData, List<RaycastResult> resultAppendList)
		{
			if (!(this.eventCamera == null))
			{
				Ray r;
				float f;
				this.ComputeRayAndDistance(eventData, out r, out f);
				if (ReflectionMethodsCache.Singleton.raycast3DAll != null)
				{
					RaycastHit[] array = ReflectionMethodsCache.Singleton.raycast3DAll(r, f, this.finalEventMask);
					if (array.Length > 1)
					{
						Array.Sort<RaycastHit>(array, (RaycastHit r1, RaycastHit r2) => r1.distance.CompareTo(r2.distance));
					}
					if (array.Length != 0)
					{
						int i = 0;
						int num = array.Length;
						while (i < num)
						{
							RaycastResult item = new RaycastResult
							{
								gameObject = array[i].collider.gameObject,
								module = this,
								distance = array[i].distance,
								worldPosition = array[i].point,
								worldNormal = array[i].normal,
								screenPosition = eventData.position,
								index = (float)resultAppendList.Count,
								sortingLayer = 0,
								sortingOrder = 0
							};
							resultAppendList.Add(item);
							i++;
						}
					}
				}
			}
		}

		// Token: 0x040000A1 RID: 161
		protected const int kNoEventMaskSet = -1;

		// Token: 0x040000A2 RID: 162
		protected Camera m_EventCamera;

		// Token: 0x040000A3 RID: 163
		[SerializeField]
		protected LayerMask m_EventMask = -1;
	}
}
 223  
UnityEngine.UI/EventSystems/PointerEventData.cs
@@ -0,0 +1,223 @@
using System;
using System.Collections.Generic;
using System.Text;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000023 RID: 35
	public class PointerEventData : BaseEventData
	{
		// Token: 0x0600009A RID: 154 RVA: 0x00003704 File Offset: 0x00001B04
		public PointerEventData(EventSystem eventSystem) : base(eventSystem)
		{
			this.eligibleForClick = false;
			this.pointerId = -1;
			this.position = Vector2.zero;
			this.delta = Vector2.zero;
			this.pressPosition = Vector2.zero;
			this.clickTime = 0f;
			this.clickCount = 0;
			this.scrollDelta = Vector2.zero;
			this.useDragThreshold = true;
			this.dragging = false;
			this.button = PointerEventData.InputButton.Left;
		}

		// Token: 0x17000023 RID: 35
		// (get) Token: 0x0600009B RID: 155 RVA: 0x00003788 File Offset: 0x00001B88
		// (set) Token: 0x0600009C RID: 156 RVA: 0x000037A2 File Offset: 0x00001BA2
		public GameObject pointerEnter { get; set; }

		// Token: 0x17000024 RID: 36
		// (get) Token: 0x0600009D RID: 157 RVA: 0x000037AC File Offset: 0x00001BAC
		// (set) Token: 0x0600009E RID: 158 RVA: 0x000037C6 File Offset: 0x00001BC6
		public GameObject lastPress { get; private set; }

		// Token: 0x17000025 RID: 37
		// (get) Token: 0x0600009F RID: 159 RVA: 0x000037D0 File Offset: 0x00001BD0
		// (set) Token: 0x060000A0 RID: 160 RVA: 0x000037EA File Offset: 0x00001BEA
		public GameObject rawPointerPress { get; set; }

		// Token: 0x17000026 RID: 38
		// (get) Token: 0x060000A1 RID: 161 RVA: 0x000037F4 File Offset: 0x00001BF4
		// (set) Token: 0x060000A2 RID: 162 RVA: 0x0000380E File Offset: 0x00001C0E
		public GameObject pointerDrag { get; set; }

		// Token: 0x17000027 RID: 39
		// (get) Token: 0x060000A3 RID: 163 RVA: 0x00003818 File Offset: 0x00001C18
		// (set) Token: 0x060000A4 RID: 164 RVA: 0x00003832 File Offset: 0x00001C32
		public RaycastResult pointerCurrentRaycast { get; set; }

		// Token: 0x17000028 RID: 40
		// (get) Token: 0x060000A5 RID: 165 RVA: 0x0000383C File Offset: 0x00001C3C
		// (set) Token: 0x060000A6 RID: 166 RVA: 0x00003856 File Offset: 0x00001C56
		public RaycastResult pointerPressRaycast { get; set; }

		// Token: 0x17000029 RID: 41
		// (get) Token: 0x060000A7 RID: 167 RVA: 0x00003860 File Offset: 0x00001C60
		// (set) Token: 0x060000A8 RID: 168 RVA: 0x0000387A File Offset: 0x00001C7A
		public bool eligibleForClick { get; set; }

		// Token: 0x1700002A RID: 42
		// (get) Token: 0x060000A9 RID: 169 RVA: 0x00003884 File Offset: 0x00001C84
		// (set) Token: 0x060000AA RID: 170 RVA: 0x0000389E File Offset: 0x00001C9E
		public int pointerId { get; set; }

		// Token: 0x1700002B RID: 43
		// (get) Token: 0x060000AB RID: 171 RVA: 0x000038A8 File Offset: 0x00001CA8
		// (set) Token: 0x060000AC RID: 172 RVA: 0x000038C2 File Offset: 0x00001CC2
		public Vector2 position { get; set; }

		// Token: 0x1700002C RID: 44
		// (get) Token: 0x060000AD RID: 173 RVA: 0x000038CC File Offset: 0x00001CCC
		// (set) Token: 0x060000AE RID: 174 RVA: 0x000038E6 File Offset: 0x00001CE6
		public Vector2 delta { get; set; }

		// Token: 0x1700002D RID: 45
		// (get) Token: 0x060000AF RID: 175 RVA: 0x000038F0 File Offset: 0x00001CF0
		// (set) Token: 0x060000B0 RID: 176 RVA: 0x0000390A File Offset: 0x00001D0A
		public Vector2 pressPosition { get; set; }

		// Token: 0x1700002E RID: 46
		// (get) Token: 0x060000B1 RID: 177 RVA: 0x00003914 File Offset: 0x00001D14
		// (set) Token: 0x060000B2 RID: 178 RVA: 0x0000392E File Offset: 0x00001D2E
		[Obsolete("Use either pointerCurrentRaycast.worldPosition or pointerPressRaycast.worldPosition")]
		public Vector3 worldPosition { get; set; }

		// Token: 0x1700002F RID: 47
		// (get) Token: 0x060000B3 RID: 179 RVA: 0x00003938 File Offset: 0x00001D38
		// (set) Token: 0x060000B4 RID: 180 RVA: 0x00003952 File Offset: 0x00001D52
		[Obsolete("Use either pointerCurrentRaycast.worldNormal or pointerPressRaycast.worldNormal")]
		public Vector3 worldNormal { get; set; }

		// Token: 0x17000030 RID: 48
		// (get) Token: 0x060000B5 RID: 181 RVA: 0x0000395C File Offset: 0x00001D5C
		// (set) Token: 0x060000B6 RID: 182 RVA: 0x00003976 File Offset: 0x00001D76
		public float clickTime { get; set; }

		// Token: 0x17000031 RID: 49
		// (get) Token: 0x060000B7 RID: 183 RVA: 0x00003980 File Offset: 0x00001D80
		// (set) Token: 0x060000B8 RID: 184 RVA: 0x0000399A File Offset: 0x00001D9A
		public int clickCount { get; set; }

		// Token: 0x17000032 RID: 50
		// (get) Token: 0x060000B9 RID: 185 RVA: 0x000039A4 File Offset: 0x00001DA4
		// (set) Token: 0x060000BA RID: 186 RVA: 0x000039BE File Offset: 0x00001DBE
		public Vector2 scrollDelta { get; set; }

		// Token: 0x17000033 RID: 51
		// (get) Token: 0x060000BB RID: 187 RVA: 0x000039C8 File Offset: 0x00001DC8
		// (set) Token: 0x060000BC RID: 188 RVA: 0x000039E2 File Offset: 0x00001DE2
		public bool useDragThreshold { get; set; }

		// Token: 0x17000034 RID: 52
		// (get) Token: 0x060000BD RID: 189 RVA: 0x000039EC File Offset: 0x00001DEC
		// (set) Token: 0x060000BE RID: 190 RVA: 0x00003A06 File Offset: 0x00001E06
		public bool dragging { get; set; }

		// Token: 0x17000035 RID: 53
		// (get) Token: 0x060000BF RID: 191 RVA: 0x00003A10 File Offset: 0x00001E10
		// (set) Token: 0x060000C0 RID: 192 RVA: 0x00003A2A File Offset: 0x00001E2A
		public PointerEventData.InputButton button { get; set; }

		// Token: 0x060000C1 RID: 193 RVA: 0x00003A34 File Offset: 0x00001E34
		public bool IsPointerMoving()
		{
			return this.delta.sqrMagnitude > 0f;
		}

		// Token: 0x060000C2 RID: 194 RVA: 0x00003A60 File Offset: 0x00001E60
		public bool IsScrolling()
		{
			return this.scrollDelta.sqrMagnitude > 0f;
		}

		// Token: 0x17000036 RID: 54
		// (get) Token: 0x060000C3 RID: 195 RVA: 0x00003A8C File Offset: 0x00001E8C
		public Camera enterEventCamera
		{
			get
			{
				return (!(this.pointerCurrentRaycast.module == null)) ? this.pointerCurrentRaycast.module.eventCamera : null;
			}
		}

		// Token: 0x17000037 RID: 55
		// (get) Token: 0x060000C4 RID: 196 RVA: 0x00003AD4 File Offset: 0x00001ED4
		public Camera pressEventCamera
		{
			get
			{
				return (!(this.pointerPressRaycast.module == null)) ? this.pointerPressRaycast.module.eventCamera : null;
			}
		}

		// Token: 0x17000038 RID: 56
		// (get) Token: 0x060000C5 RID: 197 RVA: 0x00003B1C File Offset: 0x00001F1C
		// (set) Token: 0x060000C6 RID: 198 RVA: 0x00003B37 File Offset: 0x00001F37
		public GameObject pointerPress
		{
			get
			{
				return this.m_PointerPress;
			}
			set
			{
				if (!(this.m_PointerPress == value))
				{
					this.lastPress = this.m_PointerPress;
					this.m_PointerPress = value;
				}
			}
		}

		// Token: 0x060000C7 RID: 199 RVA: 0x00003B64 File Offset: 0x00001F64
		public override string ToString()
		{
			StringBuilder stringBuilder = new StringBuilder();
			stringBuilder.AppendLine("<b>Position</b>: " + this.position);
			stringBuilder.AppendLine("<b>delta</b>: " + this.delta);
			stringBuilder.AppendLine("<b>eligibleForClick</b>: " + this.eligibleForClick);
			stringBuilder.AppendLine("<b>pointerEnter</b>: " + this.pointerEnter);
			stringBuilder.AppendLine("<b>pointerPress</b>: " + this.pointerPress);
			stringBuilder.AppendLine("<b>lastPointerPress</b>: " + this.lastPress);
			stringBuilder.AppendLine("<b>pointerDrag</b>: " + this.pointerDrag);
			stringBuilder.AppendLine("<b>Use Drag Threshold</b>: " + this.useDragThreshold);
			stringBuilder.AppendLine("<b>Current Rayast:</b>");
			stringBuilder.AppendLine(this.pointerCurrentRaycast.ToString());
			stringBuilder.AppendLine("<b>Press Rayast:</b>");
			stringBuilder.AppendLine(this.pointerPressRaycast.ToString());
			return stringBuilder.ToString();
		}

		// Token: 0x04000060 RID: 96
		private GameObject m_PointerPress;

		// Token: 0x04000066 RID: 102
		public List<GameObject> hovered = new List<GameObject>();

		// Token: 0x02000024 RID: 36
		public enum InputButton
		{
			// Token: 0x04000075 RID: 117
			Left,
			// Token: 0x04000076 RID: 118
			Right,
			// Token: 0x04000077 RID: 119
			Middle
		}

		// Token: 0x02000025 RID: 37
		public enum FramePressState
		{
			// Token: 0x04000079 RID: 121
			Pressed,
			// Token: 0x0400007A RID: 122
			Released,
			// Token: 0x0400007B RID: 123
			PressedAndReleased,
			// Token: 0x0400007C RID: 124
			NotChanged
		}
	}
}
 382  
UnityEngine.UI/EventSystems/PointerInputModule.cs
@@ -0,0 +1,382 @@
using System;
using System.Collections.Generic;
using System.Text;

namespace UnityEngine.EventSystems
{
	// Token: 0x02000028 RID: 40
	public abstract class PointerInputModule : BaseInputModule
	{
		// Token: 0x060000ED RID: 237 RVA: 0x000043C4 File Offset: 0x000027C4
		protected bool GetPointerData(int id, out PointerEventData data, bool create)
		{
			bool result;
			if (!this.m_PointerData.TryGetValue(id, out data) && create)
			{
				data = new PointerEventData(base.eventSystem)
				{
					pointerId = id
				};
				this.m_PointerData.Add(id, data);
				result = true;
			}
			else
			{
				result = false;
			}
			return result;
		}

		// Token: 0x060000EE RID: 238 RVA: 0x0000441E File Offset: 0x0000281E
		protected void RemovePointerData(PointerEventData data)
		{
			this.m_PointerData.Remove(data.pointerId);
		}

		// Token: 0x060000EF RID: 239 RVA: 0x00004434 File Offset: 0x00002834
		protected PointerEventData GetTouchPointerEventData(Touch input, out bool pressed, out bool released)
		{
			PointerEventData pointerEventData;
			bool pointerData = this.GetPointerData(input.fingerId, out pointerEventData, true);
			pointerEventData.Reset();
			pressed = (pointerData || input.phase == TouchPhase.Began);
			released = (input.phase == TouchPhase.Canceled || input.phase == TouchPhase.Ended);
			if (pointerData)
			{
				pointerEventData.position = input.position;
			}
			if (pressed)
			{
				pointerEventData.delta = Vector2.zero;
			}
			else
			{
				pointerEventData.delta = input.position - pointerEventData.position;
			}
			pointerEventData.position = input.position;
			pointerEventData.button = PointerEventData.InputButton.Left;
			base.eventSystem.RaycastAll(pointerEventData, this.m_RaycastResultCache);
			RaycastResult pointerCurrentRaycast = BaseInputModule.FindFirstRaycast(this.m_RaycastResultCache);
			pointerEventData.pointerCurrentRaycast = pointerCurrentRaycast;
			this.m_RaycastResultCache.Clear();
			return pointerEventData;
		}

		// Token: 0x060000F0 RID: 240 RVA: 0x00004518 File Offset: 0x00002918
		protected void CopyFromTo(PointerEventData from, PointerEventData to)
		{
			to.position = from.position;
			to.delta = from.delta;
			to.scrollDelta = from.scrollDelta;
			to.pointerCurrentRaycast = from.pointerCurrentRaycast;
			to.pointerEnter = from.pointerEnter;
		}

		// Token: 0x060000F1 RID: 241 RVA: 0x00004558 File Offset: 0x00002958
		protected PointerEventData.FramePressState StateForMouseButton(int buttonId)
		{
			bool mouseButtonDown = base.input.GetMouseButtonDown(buttonId);
			bool mouseButtonUp = base.input.GetMouseButtonUp(buttonId);
			PointerEventData.FramePressState result;
			if (mouseButtonDown && mouseButtonUp)
			{
				result = PointerEventData.FramePressState.PressedAndReleased;
			}
			else if (mouseButtonDown)
			{
				result = PointerEventData.FramePressState.Pressed;
			}
			else if (mouseButtonUp)
			{
				result = PointerEventData.FramePressState.Released;
			}
			else
			{
				result = PointerEventData.FramePressState.NotChanged;
			}
			return result;
		}

		// Token: 0x060000F2 RID: 242 RVA: 0x000045B8 File Offset: 0x000029B8
		protected virtual PointerInputModule.MouseState GetMousePointerEventData()
		{
			return this.GetMousePointerEventData(0);
		}

		// Token: 0x060000F3 RID: 243 RVA: 0x000045D4 File Offset: 0x000029D4
		protected virtual PointerInputModule.MouseState GetMousePointerEventData(int id)
		{
			PointerEventData pointerEventData;
			bool pointerData = this.GetPointerData(-1, out pointerEventData, true);
			pointerEventData.Reset();
			if (pointerData)
			{
				pointerEventData.position = base.input.mousePosition;
			}
			Vector2 mousePosition = base.input.mousePosition;
			if (Cursor.lockState == CursorLockMode.Locked)
			{
				pointerEventData.position = new Vector2(-1f, -1f);
				pointerEventData.delta = Vector2.zero;
			}
			else
			{
				pointerEventData.delta = mousePosition - pointerEventData.position;
				pointerEventData.position = mousePosition;
			}
			pointerEventData.scrollDelta = base.input.mouseScrollDelta;
			pointerEventData.button = PointerEventData.InputButton.Left;
			base.eventSystem.RaycastAll(pointerEventData, this.m_RaycastResultCache);
			RaycastResult pointerCurrentRaycast = BaseInputModule.FindFirstRaycast(this.m_RaycastResultCache);
			pointerEventData.pointerCurrentRaycast = pointerCurrentRaycast;
			this.m_RaycastResultCache.Clear();
			PointerEventData pointerEventData2;
			this.GetPointerData(-2, out pointerEventData2, true);
			this.CopyFromTo(pointerEventData, pointerEventData2);
			pointerEventData2.button = PointerEventData.InputButton.Right;
			PointerEventData pointerEventData3;
			this.GetPointerData(-3, out pointerEventData3, true);
			this.CopyFromTo(pointerEventData, pointerEventData3);
			pointerEventData3.button = PointerEventData.InputButton.Middle;
			this.m_MouseState.SetButtonState(PointerEventData.InputButton.Left, this.StateForMouseButton(0), pointerEventData);
			this.m_MouseState.SetButtonState(PointerEventData.InputButton.Right, this.StateForMouseButton(1), pointerEventData2);
			this.m_MouseState.SetButtonState(PointerEventData.InputButton.Middle, this.StateForMouseButton(2), pointerEventData3);
			return this.m_MouseState;
		}

		// Token: 0x060000F4 RID: 244 RVA: 0x00004734 File Offset: 0x00002B34
		protected PointerEventData GetLastPointerEventData(int id)
		{
			PointerEventData result;
			this.GetPointerData(id, out result, false);
			return result;
		}

		// Token: 0x060000F5 RID: 245 RVA: 0x00004758 File Offset: 0x00002B58
		private static bool ShouldStartDrag(Vector2 pressPos, Vector2 currentPos, float threshold, bool useDragThreshold)
		{
			return !useDragThreshold || (pressPos - currentPos).sqrMagnitude >= threshold * threshold;
		}

		// Token: 0x060000F6 RID: 246 RVA: 0x00004794 File Offset: 0x00002B94
		protected virtual void ProcessMove(PointerEventData pointerEvent)
		{
			GameObject newEnterTarget = (Cursor.lockState != CursorLockMode.Locked) ? pointerEvent.pointerCurrentRaycast.gameObject : null;
			base.HandlePointerExitAndEnter(pointerEvent, newEnterTarget);
		}

		// Token: 0x060000F7 RID: 247 RVA: 0x000047CC File Offset: 0x00002BCC
		protected virtual void ProcessDrag(PointerEventData pointerEvent)
		{
			if (pointerEvent.IsPointerMoving() && Cursor.lockState != CursorLockMode.Locked && !(pointerEvent.pointerDrag == null))
			{
				if (!pointerEvent.dragging && PointerInputModule.ShouldStartDrag(pointerEvent.pressPosition, pointerEvent.position, (float)base.eventSystem.pixelDragThreshold, pointerEvent.useDragThreshold))
				{
					ExecuteEvents.Execute<IBeginDragHandler>(pointerEvent.pointerDrag, pointerEvent, ExecuteEvents.beginDragHandler);
					pointerEvent.dragging = true;
				}
				if (pointerEvent.dragging)
				{
					if (pointerEvent.pointerPress != pointerEvent.pointerDrag)
					{
						ExecuteEvents.Execute<IPointerUpHandler>(pointerEvent.pointerPress, pointerEvent, ExecuteEvents.pointerUpHandler);
						pointerEvent.eligibleForClick = false;
						pointerEvent.pointerPress = null;
						pointerEvent.rawPointerPress = null;
					}
					ExecuteEvents.Execute<IDragHandler>(pointerEvent.pointerDrag, pointerEvent, ExecuteEvents.dragHandler);
				}
			}
		}

		// Token: 0x060000F8 RID: 248 RVA: 0x000048B4 File Offset: 0x00002CB4
		public override bool IsPointerOverGameObject(int pointerId)
		{
			PointerEventData lastPointerEventData = this.GetLastPointerEventData(pointerId);
			return lastPointerEventData != null && lastPointerEventData.pointerEnter != null;
		}

		// Token: 0x060000F9 RID: 249 RVA: 0x000048EC File Offset: 0x00002CEC
		protected void ClearSelection()
		{
			BaseEventData baseEventData = this.GetBaseEventData();
			foreach (PointerEventData currentPointerData in this.m_PointerData.Values)
			{
				base.HandlePointerExitAndEnter(currentPointerData, null);
			}
			this.m_PointerData.Clear();
			base.eventSystem.SetSelectedGameObject(null, baseEventData);
		}

		// Token: 0x060000FA RID: 250 RVA: 0x00004974 File Offset: 0x00002D74
		public override string ToString()
		{
			StringBuilder stringBuilder = new StringBuilder("<b>Pointer Input Module of type: </b>" + base.GetType());
			stringBuilder.AppendLine();
			foreach (KeyValuePair<int, PointerEventData> keyValuePair in this.m_PointerData)
			{
				if (keyValuePair.Value != null)
				{
					stringBuilder.AppendLine("<B>Pointer:</b> " + keyValuePair.Key);
					stringBuilder.AppendLine(keyValuePair.Value.ToString());
				}
			}
			return stringBuilder.ToString();
		}

		// Token: 0x060000FB RID: 251 RVA: 0x00004A38 File Offset: 0x00002E38
		protected void DeselectIfSelectionChanged(GameObject currentOverGo, BaseEventData pointerEvent)
		{
			GameObject eventHandler = ExecuteEvents.GetEventHandler<ISelectHandler>(currentOverGo);
			if (eventHandler != base.eventSystem.currentSelectedGameObject)
			{
				base.eventSystem.SetSelectedGameObject(null, pointerEvent);
			}
		}

		// Token: 0x04000083 RID: 131
		public const int kMouseLeftId = -1;

		// Token: 0x04000084 RID: 132
		public const int kMouseRightId = -2;

		// Token: 0x04000085 RID: 133
		public const int kMouseMiddleId = -3;

		// Token: 0x04000086 RID: 134
		public const int kFakeTouchesId = -4;

		// Token: 0x04000087 RID: 135
		protected Dictionary<int, PointerEventData> m_PointerData = new Dictionary<int, PointerEventData>();

		// Token: 0x04000088 RID: 136
		private readonly PointerInputModule.MouseState m_MouseState = new PointerInputModule.MouseState();

		// Token: 0x02000029 RID: 41
		protected class ButtonState
		{
			// Token: 0x17000043 RID: 67
			// (get) Token: 0x060000FD RID: 253 RVA: 0x00004A80 File Offset: 0x00002E80
			// (set) Token: 0x060000FE RID: 254 RVA: 0x00004A9B File Offset: 0x00002E9B
			public PointerInputModule.MouseButtonEventData eventData
			{
				get
				{
					return this.m_EventData;
				}
				set
				{
					this.m_EventData = value;
				}
			}

			// Token: 0x17000044 RID: 68
			// (get) Token: 0x060000FF RID: 255 RVA: 0x00004AA8 File Offset: 0x00002EA8
			// (set) Token: 0x06000100 RID: 256 RVA: 0x00004AC3 File Offset: 0x00002EC3
			public PointerEventData.InputButton button
			{
				get
				{
					return this.m_Button;
				}
				set
				{
					this.m_Button = value;
				}
			}

			// Token: 0x04000089 RID: 137
			private PointerEventData.InputButton m_Button = PointerEventData.InputButton.Left;

			// Token: 0x0400008A RID: 138
			private PointerInputModule.MouseButtonEventData m_EventData;
		}

		// Token: 0x0200002A RID: 42
		protected class MouseState
		{
			// Token: 0x06000102 RID: 258 RVA: 0x00004AE0 File Offset: 0x00002EE0
			public bool AnyPressesThisFrame()
			{
				for (int i = 0; i < this.m_TrackedButtons.Count; i++)
				{
					if (this.m_TrackedButtons[i].eventData.PressedThisFrame())
					{
						return true;
					}
				}
				return false;
			}

			// Token: 0x06000103 RID: 259 RVA: 0x00004B38 File Offset: 0x00002F38
			public bool AnyReleasesThisFrame()
			{
				for (int i = 0; i < this.m_TrackedButtons.Count; i++)
				{
					if (this.m_TrackedButtons[i].eventData.ReleasedThisFrame())
					{
						return true;
					}
				}
				return false;
			}

			// Token: 0x06000104 RID: 260 RVA: 0x00004B90 File Offset: 0x00002F90
			public PointerInputModule.ButtonState GetButtonState(PointerEventData.InputButton button)
			{
				PointerInputModule.ButtonState buttonState = null;
				for (int i = 0; i < this.m_TrackedButtons.Count; i++)
				{
					if (this.m_TrackedButtons[i].button == button)
					{
						buttonState = this.m_TrackedButtons[i];
						break;
					}
				}
				if (buttonState == null)
				{
					buttonState = new PointerInputModule.ButtonState
					{
						button = button,
						eventData = new PointerInputModule.MouseButtonEventData()
					};
					this.m_TrackedButtons.Add(buttonState);
				}
				return buttonState;
			}

			// Token: 0x06000105 RID: 261 RVA: 0x00004C20 File Offset: 0x00003020
			public void SetButtonState(PointerEventData.InputButton button, PointerEventData.FramePressState stateForMouseButton, PointerEventData data)
			{
				PointerInputModule.ButtonState buttonState = this.GetButtonState(button);
				buttonState.eventData.buttonState = stateForMouseButton;
				buttonState.eventData.buttonData = data;
			}

			// Token: 0x0400008B RID: 139
			private List<PointerInputModule.ButtonState> m_TrackedButtons = new List<PointerInputModule.ButtonState>();
		}

		// Token: 0x0200002B RID: 43
		public class MouseButtonEventData
		{
			// Token: 0x06000107 RID: 263 RVA: 0x00004C58 File Offset: 0x00003058
			public bool PressedThisFrame()
			{
				return this.buttonState == PointerEventData.FramePressState.Pressed || this.buttonState == PointerEventData.FramePressState.PressedAndReleased;
			}

			// Token: 0x06000108 RID: 264 RVA: 0x00004C84 File Offset: 0x00003084
			public bool ReleasedThisFrame()
			{
				return this.buttonState == PointerEventData.FramePressState.Released || this.buttonState == PointerEventData.FramePressState.PressedAndReleased;
			}

			// Token: 0x0400008C RID: 140
			public PointerEventData.FramePressState buttonState;

			// Token: 0x0400008D RID: 141
			public PointerEventData buttonData;
		}
	}
}
 119  
UnityEngine.UI/EventSystems/RaycastResult.cs
@@ -0,0 +1,119 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200001E RID: 30
	public struct RaycastResult
	{
		// Token: 0x1700001C RID: 28
		// (get) Token: 0x0600007A RID: 122 RVA: 0x000033F0 File Offset: 0x000017F0
		// (set) Token: 0x0600007B RID: 123 RVA: 0x0000340B File Offset: 0x0000180B
		public GameObject gameObject
		{
			get
			{
				return this.m_GameObject;
			}
			set
			{
				this.m_GameObject = value;
			}
		}

		// Token: 0x1700001D RID: 29
		// (get) Token: 0x0600007C RID: 124 RVA: 0x00003418 File Offset: 0x00001818
		public bool isValid
		{
			get
			{
				return this.module != null && this.gameObject != null;
			}
		}

		// Token: 0x0600007D RID: 125 RVA: 0x00003450 File Offset: 0x00001850
		public void Clear()
		{
			this.gameObject = null;
			this.module = null;
			this.distance = 0f;
			this.index = 0f;
			this.depth = 0;
			this.sortingLayer = 0;
			this.sortingOrder = 0;
			this.worldNormal = Vector3.up;
			this.worldPosition = Vector3.zero;
			this.screenPosition = Vector2.zero;
		}

		// Token: 0x0600007E RID: 126 RVA: 0x000034B8 File Offset: 0x000018B8
		public override string ToString()
		{
			string result;
			if (!this.isValid)
			{
				result = "";
			}
			else
			{
				result = string.Concat(new object[]
				{
					"Name: ",
					this.gameObject,
					"\nmodule: ",
					this.module,
					"\ndistance: ",
					this.distance,
					"\nindex: ",
					this.index,
					"\ndepth: ",
					this.depth,
					"\nworldNormal: ",
					this.worldNormal,
					"\nworldPosition: ",
					this.worldPosition,
					"\nscreenPosition: ",
					this.screenPosition,
					"\nmodule.sortOrderPriority: ",
					this.module.sortOrderPriority,
					"\nmodule.renderOrderPriority: ",
					this.module.renderOrderPriority,
					"\nsortingLayer: ",
					this.sortingLayer,
					"\nsortingOrder: ",
					this.sortingOrder
				});
			}
			return result;
		}

		// Token: 0x04000051 RID: 81
		private GameObject m_GameObject;

		// Token: 0x04000052 RID: 82
		public BaseRaycaster module;

		// Token: 0x04000053 RID: 83
		public float distance;

		// Token: 0x04000054 RID: 84
		public float index;

		// Token: 0x04000055 RID: 85
		public int depth;

		// Token: 0x04000056 RID: 86
		public int sortingLayer;

		// Token: 0x04000057 RID: 87
		public int sortingOrder;

		// Token: 0x04000058 RID: 88
		public Vector3 worldPosition;

		// Token: 0x04000059 RID: 89
		public Vector3 worldNormal;

		// Token: 0x0400005A RID: 90
		public Vector2 screenPosition;
	}
}
 36  
UnityEngine.UI/EventSystems/RaycasterManager.cs
@@ -0,0 +1,36 @@
using System;
using System.Collections.Generic;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200001D RID: 29
	internal static class RaycasterManager
	{
		// Token: 0x06000076 RID: 118 RVA: 0x0000337E File Offset: 0x0000177E
		public static void AddRaycaster(BaseRaycaster baseRaycaster)
		{
			if (!RaycasterManager.s_Raycasters.Contains(baseRaycaster))
			{
				RaycasterManager.s_Raycasters.Add(baseRaycaster);
			}
		}

		// Token: 0x06000077 RID: 119 RVA: 0x000033A4 File Offset: 0x000017A4
		public static List<BaseRaycaster> GetRaycasters()
		{
			return RaycasterManager.s_Raycasters;
		}

		// Token: 0x06000078 RID: 120 RVA: 0x000033BE File Offset: 0x000017BE
		public static void RemoveRaycasters(BaseRaycaster baseRaycaster)
		{
			if (RaycasterManager.s_Raycasters.Contains(baseRaycaster))
			{
				RaycasterManager.s_Raycasters.Remove(baseRaycaster);
			}
		}

		// Token: 0x04000050 RID: 80
		private static readonly List<BaseRaycaster> s_Raycasters = new List<BaseRaycaster>();
	}
}
 632  
UnityEngine.UI/EventSystems/StandaloneInputModule.cs
Large diffs are not rendered by default.

 270  
UnityEngine.UI/EventSystems/TouchInputModule.cs
@@ -0,0 +1,270 @@
using System;
using System.Collections.Generic;
using System.Text;
using UnityEngine.Serialization;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200002E RID: 46
	[Obsolete("TouchInputModule is no longer required as Touch input is now handled in StandaloneInputModule.")]
	[AddComponentMenu("Event/Touch Input Module")]
	public class TouchInputModule : PointerInputModule
	{
		// Token: 0x0600012C RID: 300 RVA: 0x00005A57 File Offset: 0x00003E57
		protected TouchInputModule()
		{
		}

		// Token: 0x1700004E RID: 78
		// (get) Token: 0x0600012D RID: 301 RVA: 0x00005A60 File Offset: 0x00003E60
		// (set) Token: 0x0600012E RID: 302 RVA: 0x00005A7B File Offset: 0x00003E7B
		[Obsolete("allowActivationOnStandalone has been deprecated. Use forceModuleActive instead (UnityUpgradable) -> forceModuleActive")]
		public bool allowActivationOnStandalone
		{
			get
			{
				return this.m_ForceModuleActive;
			}
			set
			{
				this.m_ForceModuleActive = value;
			}
		}

		// Token: 0x1700004F RID: 79
		// (get) Token: 0x0600012F RID: 303 RVA: 0x00005A88 File Offset: 0x00003E88
		// (set) Token: 0x06000130 RID: 304 RVA: 0x00005AA3 File Offset: 0x00003EA3
		public bool forceModuleActive
		{
			get
			{
				return this.m_ForceModuleActive;
			}
			set
			{
				this.m_ForceModuleActive = value;
			}
		}

		// Token: 0x06000131 RID: 305 RVA: 0x00005AAD File Offset: 0x00003EAD
		public override void UpdateModule()
		{
			this.m_LastMousePosition = this.m_MousePosition;
			this.m_MousePosition = base.input.mousePosition;
		}

		// Token: 0x06000132 RID: 306 RVA: 0x00005AD0 File Offset: 0x00003ED0
		public override bool IsModuleSupported()
		{
			return this.forceModuleActive || base.input.touchSupported;
		}

		// Token: 0x06000133 RID: 307 RVA: 0x00005B00 File Offset: 0x00003F00
		public override bool ShouldActivateModule()
		{
			bool result;
			if (!base.ShouldActivateModule())
			{
				result = false;
			}
			else if (this.m_ForceModuleActive)
			{
				result = true;
			}
			else if (this.UseFakeInput())
			{
				bool flag = base.input.GetMouseButtonDown(0);
				flag |= ((this.m_MousePosition - this.m_LastMousePosition).sqrMagnitude > 0f);
				result = flag;
			}
			else
			{
				result = (base.input.touchCount > 0);
			}
			return result;
		}

		// Token: 0x06000134 RID: 308 RVA: 0x00005B98 File Offset: 0x00003F98
		private bool UseFakeInput()
		{
			return !base.input.touchSupported;
		}

		// Token: 0x06000135 RID: 309 RVA: 0x00005BBB File Offset: 0x00003FBB
		public override void Process()
		{
			if (this.UseFakeInput())
			{
				this.FakeTouches();
			}
			else
			{
				this.ProcessTouchEvents();
			}
		}

		// Token: 0x06000136 RID: 310 RVA: 0x00005BDC File Offset: 0x00003FDC
		private void FakeTouches()
		{
			PointerInputModule.MouseState mousePointerEventData = this.GetMousePointerEventData(0);
			PointerInputModule.MouseButtonEventData eventData = mousePointerEventData.GetButtonState(PointerEventData.InputButton.Left).eventData;
			if (eventData.PressedThisFrame())
			{
				eventData.buttonData.delta = Vector2.zero;
			}
			this.ProcessTouchPress(eventData.buttonData, eventData.PressedThisFrame(), eventData.ReleasedThisFrame());
			if (base.input.GetMouseButton(0))
			{
				this.ProcessMove(eventData.buttonData);
				this.ProcessDrag(eventData.buttonData);
			}
		}

		// Token: 0x06000137 RID: 311 RVA: 0x00005C60 File Offset: 0x00004060
		private void ProcessTouchEvents()
		{
			for (int i = 0; i < base.input.touchCount; i++)
			{
				Touch touch = base.input.GetTouch(i);
				if (touch.type != TouchType.Indirect)
				{
					bool pressed;
					bool flag;
					PointerEventData touchPointerEventData = base.GetTouchPointerEventData(touch, out pressed, out flag);
					this.ProcessTouchPress(touchPointerEventData, pressed, flag);
					if (!flag)
					{
						this.ProcessMove(touchPointerEventData);
						this.ProcessDrag(touchPointerEventData);
					}
					else
					{
						base.RemovePointerData(touchPointerEventData);
					}
				}
			}
		}

		// Token: 0x06000138 RID: 312 RVA: 0x00005CE8 File Offset: 0x000040E8
		protected void ProcessTouchPress(PointerEventData pointerEvent, bool pressed, bool released)
		{
			GameObject gameObject = pointerEvent.pointerCurrentRaycast.gameObject;
			if (pressed)
			{
				pointerEvent.eligibleForClick = true;
				pointerEvent.delta = Vector2.zero;
				pointerEvent.dragging = false;
				pointerEvent.useDragThreshold = true;
				pointerEvent.pressPosition = pointerEvent.position;
				pointerEvent.pointerPressRaycast = pointerEvent.pointerCurrentRaycast;
				base.DeselectIfSelectionChanged(gameObject, pointerEvent);
				if (pointerEvent.pointerEnter != gameObject)
				{
					base.HandlePointerExitAndEnter(pointerEvent, gameObject);
					pointerEvent.pointerEnter = gameObject;
				}
				GameObject gameObject2 = ExecuteEvents.ExecuteHierarchy<IPointerDownHandler>(gameObject, pointerEvent, ExecuteEvents.pointerDownHandler);
				if (gameObject2 == null)
				{
					gameObject2 = ExecuteEvents.GetEventHandler<IPointerClickHandler>(gameObject);
				}
				float unscaledTime = Time.unscaledTime;
				if (gameObject2 == pointerEvent.lastPress)
				{
					float num = unscaledTime - pointerEvent.clickTime;
					if (num < 0.3f)
					{
						pointerEvent.clickCount++;
					}
					else
					{
						pointerEvent.clickCount = 1;
					}
					pointerEvent.clickTime = unscaledTime;
				}
				else
				{
					pointerEvent.clickCount = 1;
				}
				pointerEvent.pointerPress = gameObject2;
				pointerEvent.rawPointerPress = gameObject;
				pointerEvent.clickTime = unscaledTime;
				pointerEvent.pointerDrag = ExecuteEvents.GetEventHandler<IDragHandler>(gameObject);
				if (pointerEvent.pointerDrag != null)
				{
					ExecuteEvents.Execute<IInitializePotentialDragHandler>(pointerEvent.pointerDrag, pointerEvent, ExecuteEvents.initializePotentialDrag);
				}
			}
			if (released)
			{
				ExecuteEvents.Execute<IPointerUpHandler>(pointerEvent.pointerPress, pointerEvent, ExecuteEvents.pointerUpHandler);
				GameObject eventHandler = ExecuteEvents.GetEventHandler<IPointerClickHandler>(gameObject);
				if (pointerEvent.pointerPress == eventHandler && pointerEvent.eligibleForClick)
				{
					ExecuteEvents.Execute<IPointerClickHandler>(pointerEvent.pointerPress, pointerEvent, ExecuteEvents.pointerClickHandler);
				}
				else if (pointerEvent.pointerDrag != null && pointerEvent.dragging)
				{
					ExecuteEvents.ExecuteHierarchy<IDropHandler>(gameObject, pointerEvent, ExecuteEvents.dropHandler);
				}
				pointerEvent.eligibleForClick = false;
				pointerEvent.pointerPress = null;
				pointerEvent.rawPointerPress = null;
				if (pointerEvent.pointerDrag != null && pointerEvent.dragging)
				{
					ExecuteEvents.Execute<IEndDragHandler>(pointerEvent.pointerDrag, pointerEvent, ExecuteEvents.endDragHandler);
				}
				pointerEvent.dragging = false;
				pointerEvent.pointerDrag = null;
				if (pointerEvent.pointerDrag != null)
				{
					ExecuteEvents.Execute<IEndDragHandler>(pointerEvent.pointerDrag, pointerEvent, ExecuteEvents.endDragHandler);
				}
				pointerEvent.pointerDrag = null;
				ExecuteEvents.ExecuteHierarchy<IPointerExitHandler>(pointerEvent.pointerEnter, pointerEvent, ExecuteEvents.pointerExitHandler);
				pointerEvent.pointerEnter = null;
			}
		}

		// Token: 0x06000139 RID: 313 RVA: 0x00005F48 File Offset: 0x00004348
		public override void DeactivateModule()
		{
			base.DeactivateModule();
			base.ClearSelection();
		}

		// Token: 0x0600013A RID: 314 RVA: 0x00005F58 File Offset: 0x00004358
		public override string ToString()
		{
			StringBuilder stringBuilder = new StringBuilder();
			stringBuilder.AppendLine((!this.UseFakeInput()) ? "Input: Touch" : "Input: Faked");
			if (this.UseFakeInput())
			{
				PointerEventData lastPointerEventData = base.GetLastPointerEventData(-1);
				if (lastPointerEventData != null)
				{
					stringBuilder.AppendLine(lastPointerEventData.ToString());
				}
			}
			else
			{
				foreach (KeyValuePair<int, PointerEventData> keyValuePair in this.m_PointerData)
				{
					stringBuilder.AppendLine(keyValuePair.ToString());
				}
			}
			return stringBuilder.ToString();
		}

		// Token: 0x0400009E RID: 158
		private Vector2 m_LastMousePosition;

		// Token: 0x0400009F RID: 159
		private Vector2 m_MousePosition;

		// Token: 0x040000A0 RID: 160
		[SerializeField]
		[FormerlySerializedAs("m_AllowActivationOnStandalone")]
		private bool m_ForceModuleActive;
	}
}
 75  
UnityEngine.UI/EventSystems/UIBehaviour.cs
@@ -0,0 +1,75 @@
using System;

namespace UnityEngine.EventSystems
{
	// Token: 0x0200001F RID: 31
	public abstract class UIBehaviour : MonoBehaviour
	{
		// Token: 0x06000080 RID: 128 RVA: 0x00002058 File Offset: 0x00000458
		protected virtual void Awake()
		{
		}

		// Token: 0x06000081 RID: 129 RVA: 0x0000205B File Offset: 0x0000045B
		protected virtual void OnEnable()
		{
		}

		// Token: 0x06000082 RID: 130 RVA: 0x0000205E File Offset: 0x0000045E
		protected virtual void Start()
		{
		}

		// Token: 0x06000083 RID: 131 RVA: 0x00002061 File Offset: 0x00000461
		protected virtual void OnDisable()
		{
		}

		// Token: 0x06000084 RID: 132 RVA: 0x00002064 File Offset: 0x00000464
		protected virtual void OnDestroy()
		{
		}

		// Token: 0x06000085 RID: 133 RVA: 0x00002068 File Offset: 0x00000468
		public virtual bool IsActive()
		{
			return base.isActiveAndEnabled;
		}

		// Token: 0x06000086 RID: 134 RVA: 0x00002083 File Offset: 0x00000483
		protected virtual void OnRectTransformDimensionsChange()
		{
		}

		// Token: 0x06000087 RID: 135 RVA: 0x00002086 File Offset: 0x00000486
		protected virtual void OnBeforeTransformParentChanged()
		{
		}

		// Token: 0x06000088 RID: 136 RVA: 0x00002089 File Offset: 0x00000489
		protected virtual void OnTransformParentChanged()
		{
		}

		// Token: 0x06000089 RID: 137 RVA: 0x0000208C File Offset: 0x0000048C
		protected virtual void OnDidApplyAnimationProperties()
		{
		}

		// Token: 0x0600008A RID: 138 RVA: 0x0000208F File Offset: 0x0000048F
		protected virtual void OnCanvasGroupChanged()
		{
		}

		// Token: 0x0600008B RID: 139 RVA: 0x00002092 File Offset: 0x00000492
		protected virtual void OnCanvasHierarchyChanged()
		{
		}

		// Token: 0x0600008C RID: 140 RVA: 0x00002098 File Offset: 0x00000498
		public bool IsDestroyed()
		{
			return this == null;
		}
	}
}
 18  
UnityEngine.UI/Properties/AssemblyInfo.cs
@@ -0,0 +1,18 @@
using System;
using System.Diagnostics;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyTitle("guisystem")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("Microsoft")]
[assembly: AssemblyProduct("guisystem")]
[assembly: AssemblyCopyright("Copyright © Microsoft 2013")]
[assembly: AssemblyTrademark("")]
[assembly: InternalsVisibleTo("UnityEngine.UI.Tests")]
[assembly: ComVisible(false)]
[assembly: Guid("d4f464c7-9b15-460d-b4bc-2cacd1c1df73")]
[assembly: AssemblyFileVersion("1.0.0.0")]
0 comments on commit fac4c58
@Adminmahfuz
 
Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>
Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>
Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>
Directly mention a user or team
Reference an issue, pull request, or discussion
Add saved reply
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
 You’re not receiving notifications from this thread.
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Add files via upload · sabbir28/Unity@fac4c58
